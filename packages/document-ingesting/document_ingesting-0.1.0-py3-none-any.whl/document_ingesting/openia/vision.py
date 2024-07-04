from abc import ABC
import asyncio
import base64
from dataclasses import asdict, dataclass
import logging
from mimetypes import guess_type


from azure.core.credentials import AzureKeyCredential
from azure.core.credentials_async import AsyncTokenCredential
from jinja2 import Template
from openai import AsyncAzureOpenAI, AsyncOpenAI, RateLimitError
from openai.types.chat import (
    ChatCompletionContentPartImageParam,
    ChatCompletionContentPartTextParam,
)
from openai.types.chat.chat_completion_content_part_image_param import ImageURL
from openai_messages_token_helper import build_messages, count_tokens_for_image
from tenacity import (
    AsyncRetrying,
    retry_if_exception_type,
    stop_after_attempt,
    wait_random_exponential,
)
import tiktoken

from ..azure_helper.doc_intelligence_lite import DocFigure
from .openai_model import OpenAIModel, AzureOpenAIModelService, OpenAIModelService

logger = logging.getLogger("ingester")


@dataclass
class FigureCrop:
    fig_num: int
    height: int
    width: int
    midpoint: tuple[int, int]
    caption: str | None = None

    def as_dict(self):
        return asdict(self)


@dataclass
class PageImg:
    img_filepath: str
    page_num: int
    figure_crops: list[FigureCrop]


def local_image_to_data_url(filepath: str):
    """Encode a local image into data URL"""
    mime_type = guess_type(filepath)[0] or "application/octet-stream"
    with open(filepath, "rb") as image_file:  # Read and encode the image file
        base64_encoded_data = base64.b64encode(image_file.read()).decode("utf-8")
    return f"data:{mime_type};base64,{base64_encoded_data}"


def build_image_messages(
    model: str, sys_prompt: str, text: str, filepath: str, high_resolution: bool
):
    text_param = ChatCompletionContentPartTextParam(type="text", text=text)
    detail = "auto" if high_resolution else "low"
    img_url = ImageURL(url=local_image_to_data_url(filepath), detail=detail)
    img_param = ChatCompletionContentPartImageParam(type="image_url", image_url=img_url)
    return build_messages(
        model=model, system_prompt=sys_prompt, new_user_content=[text_param, img_param]
    )


class OpenAIVision(OpenAIModel, ABC):
    """
    Contains common logic across both OpenAI and Azure OpenAI GPT-4 vision services
    Can split chat requests into batches for more efficient GPT-4 vision calls
    """

    MAX_TOKENS = 500

    SYSTEM_PROMPT = (
        "1. Pretend to be an engineer specialised in wireless power charging; in particular the Qi Wireless standard."
        + "\n2. You will be provided an image from the Qi Wireless 1.3 standard depicting one or more figures."
        + "\n3. A patent attorney wants you inspect one of the figures and explain it to him in words. He will use your written explanation to assist him in determining whether or not one or more features of a patent claim can be mapped to the figure. He will need to do this exercise based solely on your written description of the figure and without the benefit of being able to view the figure on his computer."
        + "\n4. Your answer should start by stating the number and title of the figure."
        + "\n5. Your answer should be roughly 400-450 tokens long."
        + "\n6. There is no need to comment on the attorney's task, request or patent. The attorney simply wants your technical explanation."
        + "\n7. Make sure your answer includes comments on any text that may be present in the figure."
        + "\n8. When referring to the figure in your answer, please ensure that you cite the figure number."
        + "\n9. To indicate where the figure is located in the image, the attorney will specify the height and width of the figure (in pixels), together with the location of the figure's midpoint relative to the top-left corner of the image. The top-left corner of the image is located at pixel coordinates (0,0), wherein the first index is the row, and the second index is the column."
    )

    USER_CHAT_TEMPLATE = (
        "The middle point of the figure to describe is located in the ({{ midpoint[0] }}, {{ midpoint[1] }}) pixels and it has {{ height }} pixels in height and {{ width }} pixels in width."
        + "{% if caption %} The caption provided with the image is: '{{ caption }}'.{% endif %}"
        + "From the figures that are inside this image, ordered from top to bottom, the one to be described is the figure number {{ fig_num }}."
        + "Please proceed with your explanation for this figure."
    )

    def __init__(
        self,
        model_name: str,
        temperature: float = 0.2,
        high_resolution: bool = False,
    ):
        self.model_name = model_name
        self.temperature = temperature
        self.high_resolution = high_resolution

    def calculate_token_length(self, data: list[dict]):
        """Calculate the token length of the messages to send to the GPT-4 Vision model"""
        encoding = tiktoken.encoding_for_model(self.model_name)
        system_message = data[0]["content"]
        system_mssg_tokens = len(encoding.encode(system_message))
        user_message = data[1]["content"][0]["text"]
        user_mssg_tokens = len(encoding.encode(user_message))
        image_url = data[1]["content"][1]["image_url"]["url"]
        detail = "auto" if self.high_resolution else "low"
        image_tokens = count_tokens_for_image(image_url, detail=detail)
        return system_mssg_tokens + user_mssg_tokens + image_tokens

    def build_messages(self, fig_crop: FigureCrop, img_filepath: str):
        """Build the messages to send to the GPT-4 Vision model"""
        sys_prompt = OpenAIVision.SYSTEM_PROMPT
        img_txt_template = Template(OpenAIVision.USER_CHAT_TEMPLATE)
        img_txt = img_txt_template.render(**fig_crop.as_dict())
        return build_image_messages(
            self.model_name, sys_prompt, img_txt, img_filepath, self.high_resolution
        )

    async def create_single_completion(
        self, img_messages: list, client: AsyncOpenAI | AsyncAzureOpenAI | None = None
    ):
        """Create a completion from the GPT-4 Vision model"""
        client = client or await self.create_client()
        async for attempt in AsyncRetrying(
            retry=retry_if_exception_type(RateLimitError),
            wait=wait_random_exponential(min=15, max=60),
            stop=stop_after_attempt(15),
            before_sleep=lambda _: logger.info("Retrying due to rate limit error"),
        ):
            with attempt:
                completion = await client.chat.completions.create(
                    model=self.model_name,
                    messages=img_messages,
                    max_tokens=OpenAIVision.MAX_TOKENS,
                    temperature=self.temperature,
                )
                completion_mssg = completion.choices[0].message.content
                return completion_mssg.strip() if completion_mssg else ""

    async def execute_single_batch(
        self, input_data: list, client: AsyncOpenAI | None = None
    ):
        client = client or await self.create_client()
        return await asyncio.gather(
            *[
                self.create_single_completion(messages, client)
                for messages in input_data
            ]
        )

    async def create_descriptions(self, input_data: list[PageImg]):
        input_mssgs = [
            self.build_messages(fig_crop, img.img_filepath)
            for img in input_data
            for fig_crop in img.figure_crops
        ]
        comp_responses: list[str] = await self.create_responses(input_mssgs)
        logger.info("Extracted all completions")
        return comp_responses


class AzureOpenAIVisionService(OpenAIVision, AzureOpenAIModelService):
    """
    Class for using Azure OpenAI GPT-4 Vision
    """

    def __init__(
        self,
        model_name: str,
        open_ai_service: str,
        open_ai_deployment: str,
        credential: AsyncTokenCredential | AzureKeyCredential,
        temperature: float = 0.3,
        high_resolution: bool = False,
    ):
        super().__init__(model_name, temperature, high_resolution)
        self.open_ai_service = open_ai_service
        self.open_ai_deployment = open_ai_deployment
        self.credential = credential


class OpenAIVisionService(OpenAIVision, OpenAIModelService):
    """
    Class for using OpenAI GPT-4 Vision
    """

    def __init__(
        self,
        model_name: str,
        credential: str,
        organization: str,
        temperature: float = 0.3,
        high_resolution: bool = False,
    ):
        super().__init__(model_name, temperature, high_resolution)
        self.credential = credential
        self.organization = organization
