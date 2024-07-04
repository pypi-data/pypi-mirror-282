from abc import ABC
import base64
import re
import asyncio
from datetime import datetime
from dataclasses import dataclass, asdict
from enum import Enum
import itertools
import logging
import os


from azure.core.credentials import AzureKeyCredential
from azure.core.credentials_async import AsyncTokenCredential
from azure.search.documents.aio import SearchClient
from azure.search.documents.indexes.aio import SearchIndexClient, SearchIndexerClient
from azure.search.documents.indexes.models import (
    HnswAlgorithmConfiguration,
    HnswParameters,
    SearchableField,
    SearchField,
    SearchFieldDataType,
    SearchIndex,
    SemanticConfiguration,
    SemanticField,
    SemanticPrioritizedFields,
    SemanticSearch,
    SimpleField,
    VectorSearch,
    VectorSearchProfile,
)

from pinecone import Pinecone

# from pinecone.grpc import PineconeGRPC as Pinecone
# from pinecone.grpc.future import PineconeGrpcFuture

from .azure_helper.container_manager import ContainerManager
from .openia.embeddings import OpenAIEmbeddings
from .list_file_strategy import File
from .text_splitter import PageSplit

logger = logging.getLogger("ingester")


@dataclass(frozen=True, kw_only=True, slots=True)
class TableEntityData(ABC):
    """Dataclass to represent a table entity"""

    version: str


@dataclass(frozen=True, kw_only=True, slots=True)
class MetaInfoTableEntity(TableEntityData):
    """Dataclass to represent a table entity for the MetaInfo table"""

    RowKey: str
    name_in_db: str
    name_in_ui: str
    name_in_chart: str
    vectordb_key: str
    version: str = "2024.05-doc-int"
    PartitionKey: str = "standards"
    created_at: datetime = datetime.now()
    show_in_landscape: bool = False

    def as_dict(self):
        return asdict(self)


@dataclass(frozen=True, kw_only=True, slots=True)
class Section:
    """
    A section of a page that is stored in a search service. These sections are used as context by Azure OpenAI service
    """

    page_split: PageSplit
    filename: str
    category: str | None = None
    is_img_description: bool = False

    def as_dict(self):
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            page_split=PageSplit.from_dict(data["page_split"]),
            filename=data["filename"],
            category=data["category"],
            is_img_description=data["is_img_description"],
        )

    @property
    def filename_id(self):
        filename_ascii = re.sub("[^0-9a-zA-Z_-]", "_", self.filename)
        filename_hash = base64.b16encode(self.filename.encode("utf-8")).decode("ascii")
        return f"file-{filename_ascii}-{filename_hash}"


class SearchManagerHost(str, Enum):
    Pinecone = "pinecone"
    Azure = "azure"


class SearchManager(ABC):
    """
    Contains common logic across both OpenAI and Azure OpenAI embedding services
    Can split source text into batches for more efficient embedding calls
    """

    def __init__(
        self,
        index_name: str,
        embeddings: OpenAIEmbeddings,
    ):
        self.index_name = index_name
        self.embeddings = embeddings

    async def create_index(self, vectorizers: list | None = None):
        raise NotImplementedError

    async def update_content(self, sections: list):
        raise NotImplementedError

    async def remove_content(
        self, path: str | None = None, only_oid: str | None = None
    ):
        raise NotImplementedError


class AzureSearchManager(SearchManager):
    """
    Class to manage a search service. It can create indexes, and update or remove sections stored in these indexes
    To learn more, please visit https://learn.microsoft.com/azure/search/search-what-is-azure-search
    """

    def __init__(
        self,
        service: str,
        credential: AsyncTokenCredential | AzureKeyCredential,
        index_name: str,
        embeddings: OpenAIEmbeddings,
        search_analyzer_name: str | None = None,
    ):
        self.endpoint = f"https://{service}.search.windows.net/"
        super().__init__(index_name=index_name, embeddings=embeddings)
        self.embeddings = embeddings
        self.credential = credential
        self.search_analyzer_name = search_analyzer_name or "en.lucene"

    def create_search_client(self) -> SearchClient:
        return SearchClient(
            endpoint=self.endpoint,
            index_name=self.index_name,
            credential=self.credential,
        )

    def create_search_index_client(self) -> SearchIndexClient:
        return SearchIndexClient(endpoint=self.endpoint, credential=self.credential)

    def create_search_indexer_client(self) -> SearchIndexerClient:
        return SearchIndexerClient(endpoint=self.endpoint, credential=self.credential)

    async def create_index(self, vectorizers: list | None = None):
        logger.info("Ensuring search index %s exists", self.index_name)

        async with self.create_search_index_client() as search_index_client:
            fields = [
                SimpleField(name="id", type="Edm.String", key=True),
                SearchableField(
                    name="content",
                    type="Edm.String",
                    analyzer_name=self.search_analyzer_name,
                ),
                SearchField(
                    name="embedding",
                    type=SearchFieldDataType.Collection(SearchFieldDataType.Single),
                    hidden=False,
                    searchable=True,
                    filterable=False,
                    sortable=False,
                    facetable=False,
                    vector_search_dimensions=self.embeddings.model_name,
                    vector_search_profile_name="embedding_config",
                ),
                SimpleField(
                    name="category", type="Edm.String", filterable=True, facetable=True
                ),
                SimpleField(
                    name="sourcepage",
                    type="Edm.String",
                    filterable=True,
                    facetable=True,
                ),
                SimpleField(
                    name="sourcefile",
                    type="Edm.String",
                    filterable=True,
                    facetable=True,
                ),
            ]

            index = SearchIndex(
                name=self.index_name,
                fields=fields,
                semantic_search=SemanticSearch(
                    configurations=[
                        SemanticConfiguration(
                            name="default",
                            prioritized_fields=SemanticPrioritizedFields(
                                title_field=None,
                                content_fields=[SemanticField(field_name="content")],
                            ),
                        )
                    ]
                ),
                vector_search=VectorSearch(
                    algorithms=[
                        HnswAlgorithmConfiguration(
                            name="hnsw_config",
                            parameters=HnswParameters(metric="cosine"),
                        )
                    ],
                    profiles=[
                        VectorSearchProfile(
                            name="embedding_config",
                            algorithm_configuration_name="hnsw_config",
                            vectorizer=None,
                        ),
                    ],
                    vectorizers=vectorizers,
                ),
            )
            if self.index_name not in [
                name async for name in search_index_client.list_index_names()
            ]:
                logger.info("Creating %s search index", self.index_name)
                await search_index_client.create_index(index)
            else:
                logger.info("Search index %s already exists", self.index_name)

    async def update_content(self, sections: list[Section]):
        MAX_BATCH_SIZE = 1000
        section_batches = [
            sections[i : i + MAX_BATCH_SIZE]
            for i in range(0, len(sections), MAX_BATCH_SIZE)
        ]

        async with self.create_search_client() as search_client:
            for batch_index, batch in enumerate(section_batches):
                documents = [
                    {
                        "id": f"{section.filename_id}-page-{section_index + batch_index * MAX_BATCH_SIZE}",
                        "content": section.page_split.text,
                        "category": section.category,
                        "sourcepage": (
                            ContainerManager.sourcepage_from_file_page(
                                filename=section.filename,
                                page=section.page_split.page_num,
                            )
                        ),
                        "sourcefile": section.filename,
                    }
                    for section_index, section in enumerate(batch)
                ]
                embeddings = await self.embeddings.create_embeddings(
                    texts=[section.page_split.text for section in batch]
                )
                for i, document in enumerate(documents):
                    document["embedding"] = embeddings[i]

                await search_client.upload_documents(documents)

    async def remove_content(
        self, path: str | None = None, only_oid: str | None = None
    ):
        logger.info(
            "Removing sections from '{%s or '<all>'}' from search index '%s'",
            path,
            self.index_name,
        )
        async with self.create_search_client() as search_client:
            while True:
                filter = (
                    None
                    if path is None
                    else f"sourcefile eq '{os.path.basename(path)}'"
                )
                max_results = 1000
                result = await search_client.search(
                    search_text="",
                    filter=filter,
                    top=max_results,
                    include_total_count=True,
                )
                result_count = await result.get_count()
                if result_count == 0:
                    break
                documents_to_remove = []
                async for document in result:
                    # If only_oid is set, only remove documents that have only this oid
                    if not only_oid or document.get("oids") == [only_oid]:
                        documents_to_remove.append({"id": document["id"]})
                if len(documents_to_remove) == 0:
                    if result_count < max_results:
                        break
                    else:
                        continue
                removed_docs = await search_client.delete_documents(documents_to_remove)
                logger.info("Removed %d sections from index", len(removed_docs))
                # It can take a few seconds for search results to reflect changes, so wait a bit
                await asyncio.sleep(2)


class PineconeSearchManager(SearchManager):
    """
    Class to manage a Pinecone vector database. It can create, and update or remove embbedding of sections in the vector database
    To learn more, please visit https://www.pinecone.io/
    """

    def __init__(
        self,
        api_key: str,
        index_name: str,
        embeddings: OpenAIEmbeddings,
    ):
        super().__init__(index_name=index_name, embeddings=embeddings)
        self.api_key = api_key

    async def update_content(self, sections: list[Section], pool_threads: int = 1):
        MAX_BATCH_SIZE = 1000  # TODO: think about use another for Pinecone upload

        # Remove sections with duplicate text content
        seen_chunks = set()
        for s in sections:
            chunk_s = s.page_split.text.strip().lower()
            sections.remove(s) if chunk_s in seen_chunks else seen_chunks.add(chunk_s)

        pc = Pinecone(api_key=self.api_key, pool_threads=1)
        logger.info("Ensuring vector index %s exists", self.index_name)
        all_index_names: list[str] = pc.list_indexes().names()
        assert self.index_name in all_index_names, f"Index {self.index_name} not found"

        section_batches = itertools.batched(sections, MAX_BATCH_SIZE)
        heading2symbol = {f"Header {i}": "#" * i for i in range(1, 6)}
        for batch_index, batch in enumerate(section_batches):
            embeddings = await self.embeddings.create_embeddings(
                texts=[section.page_split.text for section in batch]
            )
            vectors_batch: list[dict] = []
            for section_index, (section, emb) in enumerate(zip(batch, embeddings, strict=True)):
                headings_dict = section.page_split.metadata or {}
                headings_str = "".join(
                    [f"{heading2symbol[k]}{v[:50]}-" for k, v in headings_dict.items()]
                )
                # TODO: consider if it's worth to include category attribute
                vectors_batch.append(
                    {
                        "id": f"{section.filename_id}-page-{section_index + batch_index * MAX_BATCH_SIZE}",
                        "values": emb,
                        "metadata": {
                            "standard": section.filename.split(".")[0],
                            "text": section.page_split.text,
                            "index": self.index_name,
                            "title": f"{headings_str}{section_index + batch_index * MAX_BATCH_SIZE}",
                            "is_image": section.is_img_description,
                        },
                    }
                )

            # Upsert data with 7 vectors per upsert request asynchronously
            # upload vectors in chunks
            with pc.Index(self.index_name, pool_threads=pool_threads) as index:
                # Send requests in parallel  # TODO: consider if it's worth to include namespace attribute
                async_results = [
                    index.upsert(vectors=list(vectors_chunk), async_req=True)
                    for vectors_chunk in itertools.batched(vectors_batch, n=7)
                ]
                # Wait for and retrieve responses (this raises in case of error)
                [async_result.get(None) for async_result in async_results]
                # if isinstance(async_result, PineconeGrpcFuture):
                # async_result.result()

    async def remove_content(self, vectors_ids: list[str] | None = None):
        logger.info(
            "Removing sections from '{%s or '<all>'}' from vector index '%s'",
            vectors_ids,
            self.index_name,
        )
        pc = Pinecone(api_key=self.api_key, pool_threads=1)
        assert (
            self.index_name in pc.list_indexes().names()
        ), f"Index {self.index_name} not found"
        index = pc.Index(self.index_name)
        delete_all = True if vectors_ids is None else False
        index.delete(ids=vectors_ids, delete_all=delete_all)
        logger.info(
            "Removed sections from '{%s or '<all>'}' from index",
            len(vectors_ids) if vectors_ids else None,
        )
        # It can take a few seconds for search results to reflect changes, so wait a bit
        await asyncio.sleep(2)

    async def create_index(self, vectorizers: list | None = None):
        raise NotImplementedError
        # logger.info("Ensuring vector index %s exists", self.index_name)
        # pc = Pinecone(api_key=self.api_key, pool_threads=1)
        # if self.index_name not in pc.list_indexes().names():
        #     pc.create_index(
        #         name=self.index_name,
        #         dimension=self.embeddings.open_ai_dimensions,
        #         spec={},  # TODO: FULLFILL THIS
        #     )
        #     logger.info("Created vector index %s", self.index_name)
        # else:
        #     logger.info("Vector index %s already exists", self.index_name)
