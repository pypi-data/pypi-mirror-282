import asyncio
from contextlib import contextmanager
from dataclasses import dataclass
import logging
import json
from pathlib import Path
from typing import Annotated, Optional, Tuple
import tempfile
import pdf2image

from azaux import ContainerManager
from azure.core.exceptions import HttpResponseError
from azure.core.credentials import AzureKeyCredential, AzureNamedKeyCredential
from azure.core.credentials_async import AsyncTokenCredential
from azure.identity.aio import AzureDeveloperCliCredential

from dotenv import load_dotenv
import pandas as pd
from rich import print
from rich.progress import Progress, SpinnerColumn, TextColumn, track
import typer

from document_ingesting.azure_helper.doc_intelligence_lite import AnalyzeResultLite
from document_ingesting.azure_helper.table_manager import TableManager
from document_ingesting.openia.openai_model import OpenAIHost
from document_ingesting.openia.embeddings import (
    AzureOpenAIEmbeddingService,
    OpenAIEmbeddingService,
)
from document_ingesting.openia.vision import (
    AzureOpenAIVisionService,
    OpenAIVisionService,
    FigureCrop,
    PageImg,
)
from document_ingesting.doc_intelligence_parser import DocIntelligenceParser

# from document_ingesting.file_strategy import FileStrategy
from document_ingesting.openia.embeddings import OpenAIEmbeddings
from document_ingesting.azure_helper.doc_intelligence_manager import (
    DocIntelligenceManager,
)
from document_ingesting.strategy import Strategy
from document_ingesting.search_manager import (
    SearchManagerHost,
    SearchManager,
    AzureSearchManager,
    PineconeSearchManager,
    Section,
    MetaInfoTableEntity,
)
from document_ingesting.doc_split import PageSplit
from document_ingesting.pdf_merger import PDFMerger
from document_ingesting.utils_files import modify_pages_by_pattern
from document_ingesting.text_splitter import SemanticTextSplitter
from document_ingesting.utils_files import write_json, pattern2list, modify_pages

# TODO: do again Q1 analysis
# TODO: study to optimize Azure Authentication
# TODO: add tests for the code
# TODO: include github actions to test the code and other CI/CD

# poetry build; pipx install dist/claims_runner-0.1.0-py3-none-any.whl
# typer document_ingesting.main utils docs --output docs/cli_manual.md --name clrun

logger = logging.getLogger("ingester")

app = typer.Typer(no_args_is_help=True, rich_markup_mode="markdown")


@dataclass
class DocIngAppState:
    """State of the Document Ingestion application to share variables accross commands"""

    azd_credential: AzureDeveloperCliCredential


def file_type_callback(value: Path | None, file_type: str):
    if value and value.suffix != f".{file_type}":
        raise typer.BadParameter(f"Only {file_type.upper()} files are supported")
    return value


@contextmanager
def rich_progress(description: str):
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        progress.add_task(description=description, total=None)
        yield progress


def setup_embeddings_service(
    openai_host: OpenAIHost,
    model_name: str,
    openai_service: str,
    openai_deployment: str,
    openai_key: str,
):
    if openai_host != OpenAIHost.openai:
        return AzureOpenAIEmbeddingService(
            model_name=model_name,
            open_ai_service=openai_service,
            open_ai_deployment=openai_deployment,
            credential=AzureKeyCredential(openai_key.strip()),
        )
    if openai_key is None:
        raise ValueError("OpenAI key is required when using the non-Azure OpenAI API")
    return OpenAIEmbeddingService(
        model_name=model_name, credential=openai_key, organization=openai_service
    )


def setup_vision_service(
    openai_host: OpenAIHost,
    openai_service: str,
    model_name: str,
    openai_deployment: str,
    openai_key: str,
    temperature: float = 0.3,
    use_high_resolution: bool = True,
):
    if openai_host != OpenAIHost.openai:
        return AzureOpenAIVisionService(
            model_name=model_name,
            open_ai_service=openai_service,
            open_ai_deployment=openai_deployment,
            credential=AzureKeyCredential(openai_key.strip()),
            temperature=temperature,
            high_resolution=use_high_resolution,
        )
    if openai_key is None:
        raise ValueError("OpenAI key is required when using the non-Azure OpenAI API")
    return OpenAIVisionService(
        model_name=model_name,
        credential=openai_key,
        organization=openai_service,
        temperature=temperature,
        high_resolution=use_high_resolution,
    )


def setup_search_manager(
    search_host: SearchManagerHost,
    search_service: str,
    index_name: str,
    embeddings: OpenAIEmbeddings,
    search_key: str,
) -> SearchManager:
    if search_host == SearchManagerHost.Pinecone:
        if search_key is None:
            raise ValueError("Search key is required when using Pinecone")
        return PineconeSearchManager(
            api_key=search_key,
            index_name=index_name,
            embeddings=embeddings,
        )
    return AzureSearchManager(
        service=search_service,
        index_name=index_name,
        embeddings=embeddings,
        credential=AzureKeyCredential(search_key.strip()),
    )


async def run_strategy(strategy: Strategy, setup_index: bool = False):
    if setup_index:
        await strategy.setup()
    result = await strategy.run()
    return result


@app.callback()
def callback(
    verbose: Annotated[
        bool,
        typer.Option(help="Verbose output", rich_help_panel="Customization and Utils"),
    ] = False,
    tenant_id: Annotated[
        str,
        typer.Option(
            help="Use this to define the Azure directory where to authenticate)",
            rich_help_panel="Azure Authentication",
            envvar="TENANT_ID",
        ),
    ] = "",
):
    """
    Document Ingestion IPMind Tool. Prepare documents by extracting content from PDFs, DOCXs, MDs or TXTs
    splitting content into sections, uploading to blob storage, and indexing in a azure search index or in
    the Pinecone vector database.
    """
    global state

    if verbose:
        logging.basicConfig(format="%(message)s")
        # We only set the level to INFO for our logger,
        # to avoid seeing the noisy INFO level logs from the Azure SDKs
    logger.setLevel(logging.INFO)

    # Load environment variables from a .env file if it exists
    load_dotenv()

    # Use the current user identity to connect to Azure services unless a key is explicitly set for any of them
    azure_credential = (
        AzureDeveloperCliCredential()
        if tenant_id is None
        else AzureDeveloperCliCredential(tenant_id=tenant_id, process_timeout=60)
    )
    state = DocIngAppState(azd_credential=azure_credential)


@app.command(
    rich_help_panel="OpenAI Vision",
    epilog=r"Example: docing describe-figs data/experims/figures_descriptions.pdf '' --temperature 0.2 --save-path 'data/experims/figures_descriptions/temp2.json'",
)
def describe_figs(
    filepath: Annotated[
        Path,
        typer.Argument(
            help="Path to the pdf with the page to be described",
            exists=True,
            dir_okay=False,
            resolve_path=True,
            callback=lambda x: file_type_callback(x, "pdf"),
        ),
    ],
    category: Annotated[
        str,
        typer.Argument(
            help="Value for the category field that will be used in the search index for all img description chunks",
            show_default=False,
        ),
    ],
    openai_service: Annotated[
        str,
        typer.Option(
            help="Name of the Azure OpenAI service used or of the organization name if not using Azure endpoints",
            envvar="OPENAI_SERVICE",
            prompt=True,
            show_default=False,
        ),
    ],
    gpt4v_deployment: Annotated[
        str,
        typer.Option(
            help="Name of the OpenAI model deployment for the vision model",
            envvar="GPT4V_DEPLOYMENT",
            prompt=True,
            show_default=False,
        ),
    ],
    pages_filter: Annotated[
        str,
        typer.Option(
            help="To specify which pages, from the ones with figures, has to be described (e.g. '1,3,5-10')",
            show_default=False,
        ),
    ] = "*",
    anl_filepath: Annotated[
        Optional[Path],
        typer.Option(
            help="Path to the JSON file with the analysis of the document",
            exists=True,
            dir_okay=False,
            resolve_path=True,
            callback=lambda x: file_type_callback(x, "json"),
        ),
    ] = None,
    save_path: Annotated[
        Optional[Path],
        typer.Option(
            help="Path to the JSON file where the image descriptions will be saved",
            dir_okay=False,
            resolve_path=True,
            callback=lambda x: file_type_callback(x, "json"),
        ),
    ] = None,
    openai_host: Annotated[
        OpenAIHost,
        typer.Option(
            help="Host of the API used to compute embeddings and image descriptions ('azure' or 'openai')",
            rich_help_panel="OpenAI",
            show_default=False,
        ),
    ] = OpenAIHost.azure,
    openai_key: Annotated[
        str,
        typer.Option(
            help="Use this Azure OpenAI account key instead of the current user identity to login",
            envvar="OPENAI_KEY",
        ),
    ] = "",
    temperature: Annotated[
        float,
        typer.Option(
            help="Temperature for the GPT-4 Vision model",
            show_default=False,
        ),
    ] = 0.3,
    high_resolution: Annotated[
        bool,
        typer.Option(
            help="Use high resolution analysis with the GPT-4 Vision model",
        ),
    ] = False,
):
    """
    **Describe** an page using the GPT-4 Vision model. :camera:
    """
    # Load Doc Int analysis from the anl_filepath JSON file
    anl_filepath = anl_filepath or filepath.with_suffix(".json")
    with rich_progress(f"Reading analysis {anl_filepath}..."):
        analysis = AnalyzeResultLite.from_json(anl_filepath)

    # Extract the pages with figures according the doc int analysis filtered if needed
    all_pages = list(range(1, len(analysis.pages) + 1))
    pages_filter_list = pattern2list(pages_filter) if pages_filter != "*" else all_pages
    all_pages_with_figs = [p for p in analysis.pages if len(p.figures) > 0]
    pages = [p for p in all_pages_with_figs if p.number in pages_filter_list]
    pages_numbers = [p.number for p in pages]

    page_images: list[PageImg] = []
    with tempfile.TemporaryDirectory() as tmp_path:
        # Create a temporary PDF with the selected pages
        figs_pdf_path = Path(tmp_path, f"{filepath.stem}_figs.pdf")
        modify_pages(filepath, pages_numbers, to_extract=True).write(figs_pdf_path)
        # Create a temporary images from the the created PDF pages
        pages_img_paths: list[str] = pdf2image.convert_from_path(
            figs_pdf_path, output_folder=tmp_path, fmt="jpeg", paths_only=True
        )  #  type: ignore
        # Create FigureCrop objects to store the data for each figure in the pages
        for img_path, page in zip(pages_img_paths, pages, strict=True):
            fig_crops: list[FigureCrop] = []
            for fig_num, fig in enumerate(page.figures):
                bbox = [round(200 * i) for i in fig.bounding_box]
                midpoint = (bbox[0] + bbox[2]) // 2, (bbox[1] + bbox[3]) // 2
                height = bbox[3] - bbox[1]
                width = bbox[2] - bbox[0]
                caption = fig.caption
                fig_crops.append(FigureCrop(fig_num, height, width, midpoint, caption))
            page_images.append(PageImg(img_path, page.number, fig_crops))

        # Create an OpenAI Vision service use it to get the image descriptions
        openai_vision_service = setup_vision_service(
            openai_host=openai_host,
            model_name=gpt4v_deployment,
            openai_service=openai_service,
            openai_deployment=gpt4v_deployment,
            openai_key=openai_key,
            temperature=temperature,
            use_high_resolution=high_resolution,
        )
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        descriptions = loop.run_until_complete(
            openai_vision_service.create_descriptions(page_images)
        )
        loop.close()

    # save the descriptions as chunks in a json file
    sections_data_list: list[dict] = []
    fig_page_nums = [p.page_num for p in page_images for _ in p.figure_crops]
    for page_num, desc_txt in zip(fig_page_nums, descriptions, strict=True):
        fig_desc_split = PageSplit(page_num=page_num, text=desc_txt)
        fig_desc_chunk = Section(
            page_split=fig_desc_split,
            filename=filepath.name,
            category=category,
            is_img_description=True,
        )
        sections_data_list.append(fig_desc_chunk.as_dict())
    descriptions_default_path = Path(filepath.parent, f"{filepath.stem}_figs.json")
    write_json(sections_data_list, save_path or descriptions_default_path)


@app.command(epilog=r"Example: docing analyze 'data/processed/VVC/vvc.pdf'")
def analyze(
    filepath: Annotated[
        Path,
        typer.Argument(
            help="Path to the PDF to be analyzed",
            exists=True,
            dir_okay=False,
            resolve_path=True,
            show_default=False,
            callback=lambda x: file_type_callback(x, "pdf"),
        ),
    ],
    doc_intelligence_service: Annotated[
        str,
        typer.Option(
            help="Name of the service for extracting text, tables and layout",
            rich_help_panel="Document Intelligence",
            envvar="DOCUMENT_INTELLIGENCE_SERVICE",
            prompt=True,
            show_default=False,
        ),
    ],
    doc_intelligence_key: Annotated[
        AsyncTokenCredential,
        typer.Option(
            help="Use this account key instead of the current user identity to login",
            rich_help_panel="Document Intelligence",
            envvar="DOCUMENT_INTELLIGENCE_KEY",
            prompt=True,
            show_default=False,
            parser=lambda x: AzureKeyCredential(x.strip()),
        ),
    ],
    save_path: Annotated[
        Optional[Path],
        typer.Option(
            exists=False,
            file_okay=True,
            dir_okay=False,
            writable=True,
            resolve_path=True,
            show_default=False,
            callback=lambda x: file_type_callback(x, "json"),
        ),
    ] = None,
    extract_figs: Annotated[
        bool,
        typer.Option(
            help="Extract Figures data from the document and save them in a json",
            show_default=False,
        ),
    ] = False,
):
    """**Analyze** a document using Document Intelligence.  :mag:"""
    doc_int_manager = DocIntelligenceManager(
        service=doc_intelligence_service, credential=doc_intelligence_key
    )
    typer.confirm(f"Proceed to the analysis of {filepath}?", abort=True)

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:  # try to analyze the document
        with rich_progress(f"Analyzing {filepath.name}..."):
            result = loop.run_until_complete(doc_int_manager.analyze_file(filepath))

    except HttpResponseError as e:  # if fails, ask to find problems in pages
        logger.error("Error analyzing the document: %s", e)
        if typer.confirm("Do you want to find the problematic pages?"):
            with rich_progress(f"Searching wrong pages..."):
                loop.run_until_complete(doc_int_manager.report_bug_pages(filepath))

    else:  # if succeeds, save the full and lite analysis and fig data locally in jsons
        print("Analysis completed successfully. :white_check_mark:")
        anl_path = save_path or Path(filepath.parent, f"{filepath.stem}.json")
        write_json(result.as_dict(), anl_path)
        print(f"Analysis saved in {anl_path}")

        # TODO: upload it instead to the Azure Blob Storage
        with rich_progress(f"Litening {filepath.name}..."):
            result_lite = AnalyzeResultLite.from_analyze_result(result)
        # create and save a lite version of the analysis
        anl_lite_path = Path(anl_path.parent, f"{anl_path.stem}_lite.json")
        result_lite.to_json(anl_lite_path)
        print(f"Lite analysis saved in {anl_lite_path}")
        # TODO convert it instead to lightweight format and save it in a local file

    finally:  #  always close the event loop at the end
        loop.close()


@app.command(
    help="**Upload** the analysis JSON to the Azure Blob Storage. :cloud:",
    epilog=r"Example: docing upload-analysis 'data/Qi/qi_doc_int-1-15_prebuilt-layout.json' --storageaccount myaccount --container mycontainer -v",
)
def upload(
    filepath: Annotated[
        Path,
        typer.Argument(
            help="Path to be uploaded",
            exists=True,
            dir_okay=False,
            resolve_path=True,
            show_default=False,
        ),
    ],
    storage_account: Annotated[
        str,
        typer.Option(
            help="Azure Blob Storage account name",
            rich_help_panel="Azure Blob Manager",
            envvar="STORAGE_ACCOUNT",
            prompt=True,
            show_default=False,
        ),
    ],
    container: Annotated[
        str,
        typer.Option(
            help="Azure Blob Storage container name",
            rich_help_panel="Azure Blob Manager",
            envvar="CONTAINER",
            prompt=True,
            show_default=False,
        ),
    ],
    storage_resource_group: Annotated[
        str,
        typer.Option(
            help="Azure Blob Storage resource group",
            rich_help_panel="Azure Blob Manager",
            envvar="STORAGE_RESOURCE_GROUP",
            prompt=True,
            show_default=False,
        ),
    ],
    storage_key: Annotated[
        AsyncTokenCredential,
        typer.Option(
            help="Use this Azure Blob Storage account key instead of the current user identity to login",
            rich_help_panel="Azure Blob Manager",
            envvar="STORAGE_KEY",
            parser=lambda x: AzureKeyCredential(x.strip()),
            prompt=True,
        ),
    ],
):
    """
    **Upload** a given file the Azure Blob Storage. :cloud:
    """
    blob_manager = ContainerManager(
        container=container,
        account=storage_account,
        credential=storage_key,
        resource_group=storage_resource_group,
    )
    # TODO: Implement the upload of the analysis JSON to the Azure Blob Storage


@app.command(
    epilog=r"Example: docing retrieve --index myindex --query 'query'",
)
def retrieve():
    """**Retrieve** data from Pinecone. :evergreen_tree:"""
    raise NotImplementedError("This command is not implemented yet")
    # TODO: Implement this function


@app.command(
    epilog=r"Example: docing chunk data/processed/AV1/av1_doc_int.json 'AV1-DOC-INT'",
)
def chunk(
    filepath: Annotated[
        Path,
        typer.Argument(
            help="Path to the analysis JSON to be ingested",
            exists=True,
            dir_okay=False,
            resolve_path=True,
            show_default=False,
            callback=lambda x: file_type_callback(x, "json"),
        ),
    ],
    category: Annotated[
        str,
        typer.Argument(
            help="Value for the category field in the search index for all sections indexed in this run",
            show_default=False,
        ),
    ],
):
    """
    **Ingest** documents by using the analysis JSON to be ingested, splitting text content into
    sections and saving them in a JSON file. :page_with_curl:
    """
    doc_int_parser = DocIntelligenceParser()

    with rich_progress(f"Reading {filepath.name}..."):
        anl_result = AnalyzeResultLite.from_json(filepath)

    # Parse the document from the analysis and split it into chunks
    pages = doc_int_parser.get_parsed_analysis(anl_result)
    splitter = SemanticTextSplitter()
    chunks = [
        Section(page_split=spl, filename=filepath.name, category=category)
        for spl in splitter.split_pages(pages)
        if spl.text
    ]
    if not chunks:
        return print("No sections found in the document. :x:")
    # save the sections in a json file
    chunks_path = Path(filepath.parent, f"{filepath.stem}_chunks.json")
    write_json([ch.as_dict() for ch in chunks], chunks_path)


@app.command(
    epilog=r"Example: docing index 'data/processed/HEVC 04.13/hevc0413_chunks.json'",
)
def index(
    filepath: Annotated[
        Path,
        typer.Argument(
            help="Path to the analysis JSON to be ingested",
            exists=True,
            dir_okay=False,
            resolve_path=True,
            show_default=False,
            callback=lambda x: file_type_callback(x, "json"),
        ),
    ],
    search_service: Annotated[
        str,
        typer.Option(
            help="Name of the Azure AI Search service where content should be indexed",
            rich_help_panel="Azure Search Manager",
            envvar="SEARCH_SERVICE",
            prompt=True,
            show_default=False,
        ),
    ],
    search_key: Annotated[
        str,
        typer.Option(
            help="Use this Pinecone key Azure AI Search account key instead of the current user identity to login",
            rich_help_panel="Search Manager",
            envvar="PINECONE_KEY",
        ),
    ],
    index: Annotated[
        str,
        typer.Option(
            help="Name of the index where content should be indexed",
            rich_help_panel="Azure Search Manager",
            envvar="INDEX",
            prompt=True,
            show_default=False,
        ),
    ],
    openai_service: Annotated[
        str,
        typer.Option(
            help="Name of the Azure OpenAI service used or of the organization name if not using Azure endpoints",
            rich_help_panel="OpenAI",
            envvar="OPENAI_SERVICE",
            prompt=True,
            show_default=False,
        ),
    ],
    emb_model: Annotated[
        str,
        typer.Option(
            help="Name of the model and of the (Azure) OpenAI model for an embedding model",
            rich_help_panel="OpenAI",
            envvar="OPENAI_EMB_MODEL_NAME",
            prompt=True,
            show_default=False,
        ),
    ],
    emb_deployment: Annotated[
        str,
        typer.Option(
            help="Name of the deployment and of the (Azure) OpenAI for an embedding model",
            rich_help_panel="OpenAI",
            envvar="OPENAI_EMB_DEPLOYMENT",
            prompt=True,
            show_default=False,
        ),
    ],
    openai_key: Annotated[
        str,
        typer.Option(
            help="Use this Azure OpenAI account key instead of the current user identity to login",
            rich_help_panel="OpenAI",
            envvar="OPENAI_KEY",
        ),
    ],
    search_host: Annotated[
        SearchManagerHost,
        typer.Option(
            help="Host of the API used to compute the search ('azure' or 'pinecone')",
            rich_help_panel="Search Manager",
            show_default=False,
        ),
    ] = SearchManagerHost.Pinecone,
    openai_host: Annotated[
        OpenAIHost,
        typer.Option(
            help="Host of the API used to compute embeddings and image descriptions ('azure' or 'openai')",
            rich_help_panel="OpenAI",
            show_default=False,
        ),
    ] = OpenAIHost.azure,
):
    """
    **Index** the sections of a document in a search index or in Pinecone. :mag_right:
    """
    with open(filepath, "rb") as f:
        sections = [Section.from_dict(section) for section in json.load(f)]
    if not sections:
        return print("No sections found in the JSON file. :x:")

    openai_embeddings_service = setup_embeddings_service(
        openai_host=openai_host,
        openai_service=openai_service,
        model_name=emb_model,
        openai_deployment=emb_deployment,
        openai_key=openai_key,
    )
    search_manager = setup_search_manager(
        search_host=search_host,
        search_service=search_service,
        index_name=index,
        embeddings=openai_embeddings_service,
        search_key=search_key,
    )

    typer.confirm(f"Proceed to the upload of {len(sections)} sections?", abort=True)
    print(f"Uploading {filepath.stem} chunks to Pinecone ...")
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(search_manager.update_content(sections))
    loop.close()
    print("Upload completed. :white_check_mark:")


@app.command(epilog="Example: docing upload-table 'hevc0413'")
def upload_table(
    standard: Annotated[
        str,
        typer.Argument(
            help="The standard to which the table belongs",
            show_default=False,
        ),
    ],
    storage_account: Annotated[
        str,
        typer.Option(
            help="Azure Blob Storage account name",
            envvar="IPMIND_STORAGE_ACCOUNT",
            prompt=True,
            show_default=False,
        ),
    ],
    table: Annotated[
        str,
        typer.Option(
            help="Azure Table name",
            envvar="IPMIND_TABLE",
            prompt=True,
            show_default=False,
        ),
    ],
    storage_key: Annotated[
        str,
        typer.Option(
            help="Use this Azure Blob Storage account key instead of the current user identity to login",
            envvar="IPMIND_STORAGE_KEY",
            prompt=True,
        ),
    ],
):
    """
    Upload a table with standard metadata to the IPMind Azure Table Storage. :cloud:
    """
    table_manager = TableManager(
        account=storage_account,
        table=table,
        credential=AzureNamedKeyCredential(storage_account, storage_key.strip()),
    )
    table_entity = MetaInfoTableEntity(
        version="2024.06-doc-int",
        RowKey=f"{standard.upper()} 2024.06 (doc-int)",
        PartitionKey="standards",
        name_in_db=f"{standard}_doc_int",
        name_in_ui=f"{standard.upper()} 2024.06",
        name_in_chart=f"{standard.upper()}",
        vectordb_key=f"{standard}_doc_int",
    )
    typer.confirm(f"Proceed to the upload of {table_entity.name_in_db}?", abort=True)
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(table_manager.upsert_entity(table_entity.as_dict()))
    loop.close()
    print(f"Table {table_entity.name_in_db} uploaded. :white_check_mark:")


@app.command()
def delete(
    filepath: Annotated[
        str, typer.Argument(help="The username to be **deleted**", show_default=False)
    ],
    all: Annotated[
        bool,
        typer.Option(help="Execute the complete **deletion of all files** :boom:"),
    ] = False,
):
    """**Delete** a certain document given its *filepath*. :fire:"""
    pass  # TODO: Implement this function


# TODO: Implement same but with pages list int
@app.command(
    rich_help_panel="PDF Utils",
    epilog="Example: docing modpages 'data/raw/VVC/vvc.pdf' '1-2,5-15,68,69,90,97,100,113,219,223,286,292,311,327,329,364,510,536-538'",
)
def modpages(
    filepath: Annotated[
        Path,
        typer.Argument(
            exists=True,
            dir_okay=False,
            writable=True,
            resolve_path=True,
            show_default=False,
            callback=lambda x: file_type_callback(x, "pdf"),
        ),
    ],
    pages: Annotated[
        str,
        typer.Argument(
            help="Start splitting all files from this page number",
            show_default=False,
        ),
    ],
    save_path: Annotated[
        Optional[Path],
        typer.Option(
            help="The default value is in data/processed inside the same parent folder as the original file",
            dir_okay=False,
            writable=True,
            resolve_path=True,
            show_default=False,
        ),
    ] = None,
    to_extract: Annotated[
        bool,
        typer.Option(
            help="Extract the pages instead of removing them",
        ),
    ] = False,
):
    """**Modify** a set of pages from a PDF file and save the result to a new file. :wrench:"""
    # Create output path
    default_output_path = Path(
        "data/processed", filepath.parent.name, filepath.name
    ).resolve()
    output_path = (save_path or default_output_path).resolve()
    if output_path.exists():
        output_path = output_path.parent / f"{output_path.stem}_mod.pdf"
    output_path.parent.mkdir(exist_ok=True, parents=True)
    # Remove or extractpages from the PDF
    modify_pages_by_pattern(filepath, pages, to_extract).write(output_path)
    action_str = "Extracted" if to_extract else "Removed"
    print(
        f"{action_str} pages {pages} \nfrom {filepath} and \nsaved in {output_path}\n"
    )


@app.command(
    rich_help_panel="PDF Utils",
    epilog="Example: docing modpages-file 'data/processed/pages_removed.csv' filter-by standard qi201",
)
def modpages_files(
    filepath: Annotated[
        Path,
        typer.Argument(
            help="Path to the CSV file with the list of files in which pages have to be modified",
            exists=True,
            dir_okay=False,
            resolve_path=True,
            show_default=False,
            callback=lambda x: file_type_callback(x, "csv"),
        ),
    ],
    pages_col: Annotated[
        str,
        typer.Option(help="Column name in the CSV file of the pages to be modified"),
    ] = "pages",
    paths_col: Annotated[
        str,
        typer.Option(help="Column name in the CSV file of the PDF filepaths"),
    ] = "filepath",
    to_extract: Annotated[
        bool,
        typer.Option(help="Extract the pages instead of removing them"),
    ] = False,
    filter_by: Annotated[
        Tuple[str, str],
        typer.Option(
            help="Column name and value to filter the files to be modified",
            show_default=False,
        ),
    ] = ("", ""),
):
    """
    **Modify** a set of pages from a list of PDF files and save the results to new files. :wrench:
    """
    modpages_df = pd.read_csv(filepath)
    # Filter the files to be modified and set their filepaths as the df index
    if filter_by[0]:  # for col, val in to_filter or []:
        col, val = filter_by
        modpages_df = modpages_df[modpages_df.pop(col) == val]
    modpages_df.set_index(paths_col, inplace=True)
    # Modify the pages in the PDF files
    for fp, pages in modpages_df[pages_col].items():
        modpages(Path(str(fp)), pages, to_extract=to_extract)


@app.command(rich_help_panel="PDF Utils")
def merge_pdfs(
    folder: Annotated[
        Path,
        typer.Argument(
            exists=True,
            file_okay=False,
            writable=True,
            resolve_path=True,
            show_default=False,
        ),
    ],
    save_path: Annotated[
        Optional[Path],
        typer.Option(
            dir_okay=False,
            writable=True,
            resolve_path=True,
            show_default=False,
        ),
    ] = None,
    from_page: Annotated[
        int,
        typer.Option(
            help="Start merging all files from this page number",
            show_default=False,
        ),
    ] = 0,
    save_removed: Annotated[
        bool,
        typer.Option(
            help="Save two PDFs with the pages that have been filtered (use this for research purposes)",
            show_default=False,
        ),
    ] = True,
    use_simple: Annotated[
        bool,
        typer.Option(
            help="Use a simple merge without removing duplicate pages",
            show_default=False,
        ),
    ] = False,
):
    """**Merge PDFs** in FOLDER into a single PDF, removing duplicate pages based on content. :page_facing_up:"""
    pdf_merger = PDFMerger(simple_merge=use_simple)
    for filepath in track(list(folder.glob("*.pdf")), description="Merging PDFs..."):
        pdf_merger.from_file(filepath, from_page=from_page)
    suffix = "_simple" if use_simple else ""
    output_path = Path(save_path or Path(folder.parent, f"{folder.name}{suffix}.pdf"))
    pdf_merger.save_pages(pdf_merger.seen_pages, output_path)

    if save_removed:  # Save all the pages that have been filtered out
        if pdf_merger.initial_pages:  # Save the initial pages
            init_pages_path = output_path.with_name(f"{output_path.stem}_initial.pdf")
            pdf_merger.save_pages(pdf_merger.initial_pages, init_pages_path)
            print(f"Initial pages saved in {init_pages_path}")
        if pdf_merger.duplicate_pages:  # Save the duplicate pages in dedicated folders
            dupl_pages_folder = output_path.with_name(f"{output_path.stem}_duplicates")
            dupl_pages_folder.mkdir(exist_ok=True)
            for page_number, pages in pdf_merger.duplicate_pages.items():
                orig_page = pdf_merger.seen_pages[page_number]
                dupl_folder = dupl_pages_folder / str(orig_page)
                dupl_folder.mkdir(exist_ok=True)
                pdf_merger.save_pages(
                    [orig_page], dupl_folder / f"orig - {orig_page}.pdf"
                )
                pdf_merger.save_pages(pages, dupl_folder / f"dupls - {orig_page}.pdf")
            print(f"Duplicate pages saved in {dupl_pages_folder}")


if __name__ == "__main__":
    import os

    # SEARCH_SERVICE = os.getenv("SEARCH_SERVICE") or ""
    # PINECONE_KEY = os.getenv("PINECONE_KEY") or ""
    # INDEX = os.getenv("INDEX") or ""
    OPENAI_SERVICE = os.getenv("OPENAI_SERVICE") or ""
    # OPENAI_EMB_MODEL_NAME = os.getenv("OPENAI_EMB_MODEL_NAME") or ""
    # OPENAI_EMB_DEPLOYMENT = os.getenv("OPENAI_EMB_DEPLOYMENT") or ""
    OPENAI_KEY = os.getenv("OPENAI_KEY") or ""
    GPT4V_DEPLOYMENT = os.getenv("GPT4V_DEPLOYMENT") or ""
    # chunk(filepath, category)
    # index(
    #     filepath,
    #     SEARCH_SERVICE,
    #     PINECONE_KEY,
    #     INDEX,
    #     OPENAI_SERVICE,
    #     OPENAI_EMB_MODEL_NAME,
    #     OPENAI_EMB_DEPLOYMENT,
    #     OPENAI_KEY,
    # )
    filepath = Path("data/experims/to_desc_figs.pdf")
    category = "Qi2-DOC-INT"
    anl_filepath = Path("data/experims/to_desc_figs.json")
    describe_figs(
        filepath,
        category,
        OPENAI_SERVICE,
        GPT4V_DEPLOYMENT,
        openai_host=OpenAIHost.azure,
        openai_key=OPENAI_KEY,
        anl_filepath=anl_filepath,
        # pages_filter="1,2",
    )
