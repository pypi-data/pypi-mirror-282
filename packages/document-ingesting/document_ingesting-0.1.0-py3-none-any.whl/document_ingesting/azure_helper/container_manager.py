from contextlib import asynccontextmanager
import logging
import os
import re

from azure.core.credentials_async import AsyncTokenCredential
from azure.storage.blob.aio import BlobServiceClient

from document_ingesting.azure_helper.resource_manager import (
    StorageResource,
    StorageResourceType,
)
from ..list_file_strategy import File

logger = logging.getLogger("ingester")


class ContainerManager(StorageResource):
    """
    Class to manage uploading and deleting blobs containing citation information from a blob storage account
    """

    def __init__(
        self,
        account: str,
        container: str,
        credential: AsyncTokenCredential,
        resource_group: str,
    ):
        self.resource_group = resource_group
        self.container = container
        super().__init__(account, credential)

    @property
    def resource_type(self) -> StorageResourceType:
        return StorageResourceType.BLOB

    @asynccontextmanager
    async def get_client(self, **kwargs):
        async with BlobServiceClient(
            self.endpoint, self.storage.credential, **kwargs
        ) as service_client:
            yield service_client.get_container_client(self.container)

    @asynccontextmanager
    async def get_blob_client(self, filepath: str):
        async with self.get_client() as container_client:
            yield container_client.get_blob_client(filepath)

    async def upload_blob(self, file: File) -> list[str] | None:
        async with self.get_client(
            max_single_put_size=4 * 1024 * 1024
        ) as container_client:
            if not await container_client.exists():
                await container_client.create_container()
            # open and upload the original file
            with open(file.content.name, "rb") as reopened_file:
                blob_name = ContainerManager.blob_name_from_file_name(file.content.name)
                logger.info("Uploading blob for whole file -> %s", blob_name)
                await container_client.upload_blob(
                    blob_name, reopened_file, overwrite=True
                )
        return None

    async def remove_blob(self, path: str | None = None):
        async with self.get_client() as container_client:
            if not await container_client.exists():
                return
            if path is None:
                prefix = None
                blobs = container_client.list_blob_names()
            else:
                prefix = os.path.splitext(os.path.basename(path))[0]
                blobs = container_client.list_blob_names(
                    name_starts_with=os.path.splitext(os.path.basename(prefix))[0]
                )
            async for blob_path in blobs:
                # This still supports PDFs split into individual pages, but we could remove in future to simplify code
                if (
                    prefix is not None
                    and (
                        not re.match(rf"{prefix}-\d+\.pdf", blob_path)
                        or not re.match(rf"{prefix}-\d+\.png", blob_path)
                    )
                ) or (path is not None and blob_path == os.path.basename(path)):
                    continue
                logger.info("Removing blob %s", blob_path)
                await container_client.delete_blob(blob_path)

    @classmethod
    def sourcepage_from_file_page(cls, filename, page=0) -> str:
        if os.path.splitext(filename)[1].lower() == ".pdf":
            return f"{os.path.basename(filename)}#page={page+1}"
        else:
            return os.path.basename(filename)

    @classmethod
    def blob_name_from_file_name(cls, filename) -> str:
        return os.path.basename(filename)
