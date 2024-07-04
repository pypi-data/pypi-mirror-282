from abc import ABC, abstractmethod
from enum import Enum
import logging
from typing import Any, Awaitable, Callable
from typing_extensions import TypedDict

from azure.core.credentials import AzureKeyCredential
from azure.core.credentials_async import AsyncTokenCredential
from azure.identity.aio import get_bearer_token_provider
from openai import AsyncAzureOpenAI, AsyncOpenAI
from openai_messages_token_helper import get_token_limit

logger = logging.getLogger("ingester")


class OpenAIHost(str, Enum):
    openai = "openai"
    azure = "azure"


class TokenBatch:
    """
    Represents a batch of the data that is going to be passed to the OpenAI API

    Args:
        texts: List of data to be passed to the OpenAI API
        token_length: Total token length of the data in the batch
    """

    def __init__(self, data: list, token_length: int):
        self.data = data
        self.token_length = token_length


class OpenAIModel(ABC):
    """
    Contains common logic across both OpenAI and Azure OpenAI model services
    Can split data into batches for more efficient API calls
    """

    MODELS_BATCH_INFO = {
        "text-embedding-ada-002": {"token_limit": 8100, "max_batch_size": 16},
        "gpt-4": {"token_limit": 8100, "max_batch_size": 16},  # TODO: Check this
        "gpt-4o": {"token_limit": 8100, "max_batch_size": 16},
    }

    def __init__(self, model_name: str) -> None:
        self.model_name = model_name

    @abstractmethod
    async def create_client(self) -> AsyncOpenAI:
        raise NotImplementedError

    @abstractmethod
    def calculate_token_length(self, data: Any):
        raise NotImplementedError

    def split_into_batches(self, data: list) -> list[TokenBatch]:
        """
        Split the data into batches based on the token limit and max batch size of the model
        """
        batch_info = OpenAIModel.MODELS_BATCH_INFO.get(self.model_name)
        if not batch_info:
            raise NotImplementedError(f"Not support batching for {self.model_name}")
        batch_token_limit = batch_info["token_limit"]
        batch_max_size = batch_info["max_batch_size"]

        token_batches: list[TokenBatch] = []
        batch_items = []
        batch_token_length = 0
        for item in data:
            text_token_length = self.calculate_token_length(item)
            if (
                batch_token_length + text_token_length >= batch_token_limit
                and len(batch_items) > 0
            ):
                token_batches.append(TokenBatch(batch_items, batch_token_length))
                batch_items = []
                batch_token_length = 0

            batch_items.append(item)
            batch_token_length = batch_token_length + text_token_length
            if len(batch_items) == batch_max_size:
                token_batches.append(TokenBatch(batch_items, batch_token_length))
                batch_items = []
                batch_token_length = 0

        if len(batch_items) > 0:
            token_batches.append(TokenBatch(batch_items, batch_token_length))

        return token_batches

    @abstractmethod
    async def execute_single_batch(
        self, input_data: list, client: AsyncOpenAI | None = None
    ):
        raise NotImplementedError

    async def create_responses(self, input_data: list) -> list:
        batches = self.split_into_batches(input_data)
        responses_data = []
        client = await self.create_client()
        for batch in batches:
            resp_data = await self.execute_single_batch(batch.data, client)
            responses_data.extend(resp_data)
            logger.info(
                "Computed responses in batch. Batch size: %d, Token count: %d with model %s",
                len(batch.data),
                batch.token_length,
                self.model_name,
            )
        return responses_data


class AzureOpenAIModelService(OpenAIModel, ABC):
    """
    Class for using Azure OpenAI models
    """

    # API_VERSION = "2024-02-01"
    API_VERSION = "2023-05-15"

    def __init__(
        self,
        model_name: str,
        open_ai_service: str,
        open_ai_deployment: str,
        credential: AsyncTokenCredential | AzureKeyCredential,
    ):
        self.model_name = model_name
        self.open_ai_service = open_ai_service
        self.open_ai_deployment = open_ai_deployment
        self.credential = credential

    async def create_client(self) -> AsyncOpenAI:
        class AuthArgs(TypedDict, total=False):
            api_key: str
            azure_ad_token_provider: Callable[[], str | Awaitable[str]]

        auth_args = AuthArgs()
        if isinstance(self.credential, AzureKeyCredential):
            auth_args["api_key"] = self.credential.key
        elif isinstance(self.credential, AsyncTokenCredential):
            auth_args["azure_ad_token_provider"] = get_bearer_token_provider(
                self.credential, "https://cognitiveservices.azure.com/.default"
            )
        else:
            raise TypeError("Invalid credential type")

        return AsyncAzureOpenAI(
            azure_endpoint=f"https://{self.open_ai_service}.openai.azure.com",
            azure_deployment=self.open_ai_deployment,
            api_version=AzureOpenAIModelService.API_VERSION,
            **auth_args,  # type: ignore
        )


class OpenAIModelService(OpenAIModel, ABC):
    """
    Class for using OpenAI Models
    """

    def __init__(
        self,
        model_name: str,
        credential: str,
        organization: str,
    ):
        self.model_name = model_name
        self.credential = credential
        self.organization = organization

    async def create_client(self) -> AsyncOpenAI:
        return AsyncOpenAI(api_key=self.credential, organization=self.organization)
