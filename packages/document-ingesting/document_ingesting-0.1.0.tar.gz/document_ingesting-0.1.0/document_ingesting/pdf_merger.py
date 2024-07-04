from dataclasses import dataclass
import logging
from pathlib import Path
import tempfile

import imagehash
from imagehash import ImageHash
import pdf2image
from pypdf import PdfReader, PdfWriter
from pypdf._page import PageObject
from collections import defaultdict

logger = logging.getLogger("ingester")


@dataclass(frozen=True, kw_only=True, slots=True)
class PDFPage:
    file_name: str
    page: PageObject
    img_hash: ImageHash | None = None

    def __eq__(self, other):
        if not self.img_hash or not other.img_hash:
            raise ValueError("Image hash is required to compare PDF pages.")
        return self.img_hash == other.img_hash

    def __str__(self):
        return f"{self.file_name}-{self.page.page_number}"


class PDFMerger:
    """Module to merge PDF files without adding duplicate pages."""

    def __init__(self, simple_merge: bool = False):
        self.simple_merge = simple_merge
        self.seen_pages: list[PDFPage] = []
        self.duplicate_pages: dict[int, list[PDFPage]] = defaultdict(list)
        self.initial_pages: list[PDFPage] = []

    def from_page(self, pdf_page: PDFPage, from_page: int = 0):
        """Add a page to the merged PDF if it is not a duplicate."""
        if pdf_page.page.page_number is None:
            raise ValueError("Page number is required to merge PDFs.")
        if pdf_page.page.page_number < from_page:
            self.initial_pages.append(pdf_page)
        elif pdf_page in self.seen_pages:
            page_ind = self.seen_pages.index(pdf_page)
            page_duplicated = self.seen_pages[page_ind]
            if self.simple_merge:
                logger.warning(f"Page {page_ind} dupl with {len(self.seen_pages)}.")
                self.seen_pages.append(pdf_page)
            else:
                logger.info(f"Page {page_duplicated} dupl with {pdf_page}")
                self.duplicate_pages[page_ind].append(pdf_page)
        else:  # Only if the page is not a duplicate add it to the merged PDF
            self.seen_pages.append(pdf_page)  # TODO

    def from_file(self, pdf_path: Path, from_page: int = 0):
        """Add all pages from a PDF file to the merged PDF."""
        reader = PdfReader(pdf_path)

        for page in reader.pages[:from_page]:  # track removed initial pages
            init_page = PDFPage(file_name=pdf_path.stem, page=page)
            self.initial_pages.append(init_page)

        with tempfile.TemporaryDirectory() as tmp_path:
            page_imgs = pdf2image.convert_from_path(pdf_path, output_folder=tmp_path)
            for img, page in zip(page_imgs[from_page:], reader.pages[from_page:], strict=True):
                img_hash = imagehash.average_hash(img, hash_size=32)
                self.from_page(
                    PDFPage(file_name=pdf_path.stem, page=page, img_hash=img_hash)
                )

    def from_folder(self, folder_path: Path, from_page: int = 0):
        """Add all pages from all PDF files in a folder to the merged PDF."""
        for pdf_path in folder_path.glob("*.pdf"):
            self.from_file(pdf_path, from_page)

    @staticmethod
    def save_pages(pdf_pages: list[PDFPage], save_path: Path):
        """Save a list of PDF pages to a file. If the file already exists, overwrite it."""
        pdf_writer = PdfWriter()
        for page in pdf_pages:
            pdf_writer.add_page(page.page)
        if save_path.exists():
            logger.warning(f"File {save_path} already exists. Overwriting it.")
            save_path.unlink()
        with open(save_path, "wb") as f:
            pdf_writer.write(f)
