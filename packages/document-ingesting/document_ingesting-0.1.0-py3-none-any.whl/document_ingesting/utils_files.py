from pathlib import Path
from pypdf import PdfReader, PdfWriter
import json


def read_json(filepath: str | Path):
    """Read a JSON file and return its content."""
    with open(filepath, "r") as f:
        return json.load(f)


def write_json(data: dict | list, filepath: str | Path):
    """Write a dictionary to a JSON file."""
    with open(filepath, "w") as f:
        json.dump(data, f)


def modify_pages(filepath: str | Path, pages: list[int], to_extract: bool = False):
    """Extract or remove a range of pages from a PDF file and save the result to a new file."""
    reader = PdfReader(filepath)
    writer = PdfWriter()
    for page_num, page in enumerate(reader.pages, start=1):
        if not to_extract and page_num not in pages:
            writer.add_page(page)
        elif to_extract and page_num in pages:
            writer.add_page(page)
    return writer


def pattern2list(pattern: str) -> list[int]:
    """Convert a pattern of pages to a list of integers."""
    pattern_list = []
    for pt_split in pattern.split(","):
        if "-" in pt_split:
            start, end = pt_split.split("-")
            pattern_list.extend(range(int(start.strip()), int(end.strip()) + 1))
        else:
            pattern_list.append(int(pt_split.strip()))
    return pattern_list


def modify_pages_by_pattern(filepath: str | Path, pages: str, to_extract: bool = False):
    """Remove or extract a pattern of pages from a PDF file and save the result to a new file."""
    return modify_pages(filepath, pages=pattern2list(pages), to_extract=to_extract)


def split_pdf_by_range(filepath: str | Path, start: int, end: int):
    """Split a PDF file into a range of pages and save the result to a new file."""
    return modify_pages(filepath, list(range(start, end + 1)), to_extract=True)
