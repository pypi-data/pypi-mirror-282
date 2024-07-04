from abc import ABC, abstractmethod
import logging

import tiktoken
from azure.core.credentials import AzureKeyCredential
from azure.core.credentials_async import AsyncTokenCredential
from openai import AsyncOpenAI, RateLimitError
from tenacity import (
    AsyncRetrying,
    retry_if_exception_type,
    stop_after_attempt,
    wait_random_exponential,
)

from .openai_model import OpenAIModel, AzureOpenAIModelService, OpenAIModelService

logger = logging.getLogger("ingester")


class OpenAIEmbeddings(OpenAIModel, ABC):
    """
    Contains common logic across both OpenAI and Azure OpenAI embedding services
    Can split source text into batches for more efficient embedding calls
    """

    def __init__(self, model_name: str):
        self.model_name = model_name

    async def execute_single_batch(
        self, texts: list[str], client: AsyncOpenAI | None = None
    ):
        async for attempt in AsyncRetrying(
            retry=retry_if_exception_type(RateLimitError),
            wait=wait_random_exponential(min=15, max=60),
            stop=stop_after_attempt(15),
            before_sleep=lambda _: logger.info("Retrying due to rate limit error"),
        ):
            with attempt:
                client = client or await self.create_client()
                response = await client.embeddings.create(
                    model=self.model_name, input=texts
                )
        return [emb.embedding for emb in response.data]

    def calculate_token_length(self, data: str):
        encoding = tiktoken.encoding_for_model(self.model_name)
        return len(encoding.encode(data))

    async def create_embeddings(self, texts: list[str]) -> list[list[float]]:
        embeddings: list[list[float]] = await self.create_responses(texts)
        logger.info("Extracted all embeddings successfully")
        return embeddings


class AzureOpenAIEmbeddingService(OpenAIEmbeddings, AzureOpenAIModelService):
    """
    Class for using Azure OpenAI embeddings
    To learn more please visit https://learn.microsoft.com/azure/ai-services/openai/concepts/understand-embeddings
    """

    def __init__(
        self,
        model_name: str,
        open_ai_service: str,
        open_ai_deployment: str,
        credential: AsyncTokenCredential | AzureKeyCredential,
    ):
        super().__init__(model_name)
        self.open_ai_service = open_ai_service
        self.open_ai_deployment = open_ai_deployment
        self.credential = credential


class OpenAIEmbeddingService(OpenAIEmbeddings, OpenAIModelService):
    """
    Class for using OpenAI embeddings
    To learn more please visit https://platform.openai.com/docs/guides/embeddings
    """

    def __init__(
        self,
        model_name: str,
        credential: str,
        organization: str,
    ):
        super().__init__(model_name)
        self.credential = credential
        self.organization = organization
