from contextlib import asynccontextmanager
import logging
from typing import IO
import os
from pathlib import Path

from azure.ai.documentintelligence.aio import DocumentIntelligenceClient
from azure.core.credentials import AzureKeyCredential
from azure.core.credentials_async import AsyncTokenCredential
from azure.ai.documentintelligence.aio import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import DocumentAnalysisFeature
from pypdf import PdfReader

from document_ingesting.utils_files import split_pdf_by_range

logger = logging.getLogger("ingester")


class DocIntelligenceManager:
    """
    Class to manage the Azure Document Intelligence service
    """

    MODEL_ID = "prebuilt-layout"
    LOCALE = "en"
    FEATURES: list[str | DocumentAnalysisFeature] = [DocumentAnalysisFeature.FORMULAS]
    # CONTENT_TYPE = "application/octet-stream"
    CONTENT_TYPE = "application/pdf"
    OUTPUT_CONTENT_FORMAT = "markdown"

    def __init__(
        self,
        service: str,
        credential: AsyncTokenCredential | AzureKeyCredential,
    ):
        self.service = service
        self.credential = credential

    @property
    def endpoint(self):
        return f"https://{self.service}.cognitiveservices.azure.com/"

    @asynccontextmanager
    async def get_client(self):
        async with DocumentIntelligenceClient(
            endpoint=self.endpoint, credential=self.credential
        ) as document_intelligence_client:
            yield document_intelligence_client

    async def analyze_file(self, filepath: str | Path):
        """Analyzes the given file and returns the results"""
        logger.info("Using Azure Document Intelligence in '%s' file", filepath)
        with open(filepath, "rb") as f:
            analysis_results = await self._analyze_content(f)
        return analysis_results

    async def _analyze_content(self, content: IO):
        """Analyzes the content of the given file and returns the results"""
        async with self.get_client() as document_intelligence_client:
            poller = await document_intelligence_client.begin_analyze_document(
                model_id=DocIntelligenceManager.MODEL_ID,
                analyze_request=content,
                locale=DocIntelligenceManager.LOCALE,
                features=DocIntelligenceManager.FEATURES,
                content_type=DocIntelligenceManager.CONTENT_TYPE,
                output_content_format=DocIntelligenceManager.OUTPUT_CONTENT_FORMAT,
            )
            analysis_results = await poller.result()
            return analysis_results

    # hevc: [48,78,96,163,184,186,346,358,387,421,446,678]
    # hvec0413: [32,43,126,133,140,143,150,152,182,206,264,287,289,310]
    # vvc: [68,69,90,97,100,113,219,223,286,292,311,327,329,364,510]
    # TODO: check if this is has been fixed in the latest version of the SDK
    async def report_bug_pages(self, filepath):
        """Report the pages that caused an error during the analysis"""
        self._bug_pages = []
        page_range = (1, len(PdfReader(filepath).pages))
        logger.info(f"Analyzing pages {page_range[0]}-{page_range[1]}...")
        page_mid = sum(page_range) // 2
        await self._find_bug_pages(filepath, page_range=(page_range[0], page_mid))
        await self._find_bug_pages(filepath, page_range=(page_mid + 1, page_range[1]))
        logger.warning(f"\n\nPages with errors: {",".join(self._bug_pages)}")

    async def _find_bug_pages(self, filepath: Path, page_range: tuple[int, int]):
        """Find the pages that caused an error during the analysis using binary search"""
        page_start, page_end = page_range
        split_path = filepath.parent / f"{filepath.stem}_{page_start}-{page_end}.pdf"

        # create and save a new PDF with the pages that caused an error
        pdf_splitted = split_pdf_by_range(filepath, start=page_start, end=page_end)
        pdf_splitted.write(split_path)

        try:  # try to analyze the document
            logger.info(f"Analyzing pages {page_start}-{page_end}...")
            await self.analyze_file(split_path)
            logger.info(f"Pages {page_start}-{page_end} analyzed successfully.")
        except Exception as e:  # if it fails, split pages in half and try again
            if page_start == page_end:
                logger.warning(f"\nError analyzing page {page_start}: {e}\n")
                self._bug_pages.append(page_start)
                return
            page_mid = (page_start + page_end) // 2
            await self._find_bug_pages(filepath, page_range=(page_start, page_mid))
            await self._find_bug_pages(filepath, page_range=(page_mid + 1, page_end))
        finally:  # remove the split file after the analysis
            os.remove(split_path)
