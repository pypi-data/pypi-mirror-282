import logging
from abc import ABC
import re
from typing import Generator, Set

from langchain.text_splitter import MarkdownHeaderTextSplitter
import tiktoken

from .doc_split import Page, PageSplit

logger = logging.getLogger("ingester")


def cleanup_data(data: str) -> str:
    """Cleans up the given content using regexes
    Args:
        data: (str): The data to clean up.
    Returns:
        str: The cleaned up data.
    """
    # match all lines with only whitespaces and replace them with empty string.
    data = re.sub(r"^\s+$", "", data, flags=re.MULTILINE)
    # match two or more newlines and replace them with one new lines
    data = re.sub(r"\n{2,}", "\n", data)
    # match two or more spaces that are not newlines and replace them with one space
    data = re.sub(r"[^\S\n]{2,}", " ", data)
    # remove leading and trailing whitespaces from each line
    data = "\n".join(line.strip() for line in data.splitlines())
    return data.strip()


class TextSplitter(ABC):
    """
    Splits a list of pages into smaller chunks
    :param pages: The pages to split
    :return: A generator of SplitPage
    """

    def split_pages(self, pages: list[Page]) -> Generator[PageSplit, None, None]:
        if False:
            yield  # pragma: no cover - this is necessary for mypy to type check


ENCODING_MODEL = "text-embedding-ada-002"

STANDARD_WORD_BREAKS = [",", ";", ":", " ", "(", ")", "[", "]", "{", "}", "\t", "\n"]

LATEX_FORMULA_BREAKS = ["\\"]

STANDARD_SENTENCE_ENDINGS = [".", "!", "?"]

LATEX_FORMULA_ENDINGS = ["$"]

# NB: text-embedding-3-XX is the same BPE as text-embedding-ada-002
bpe = tiktoken.encoding_for_model(ENCODING_MODEL)

DEFAULT_OVERLAP_PERCENT = 10  # See semantic search article for 10% overlap performance
DEFAULT_SECTION_LENGTH = 1000  # Roughly 400-500 tokens for English


class SectionAndSentenceTextSplitter(TextSplitter):
    """
    Class that splits pages into smaller chunks. This is required because embedding models may not be able to analyze an entire page at once
    """

    def __init__(self, max_tokens_per_section: int = 500):
        self.sentence_text_splitter = SentenceTextSplitter(max_tokens_per_section)


class SentenceTextSplitter(TextSplitter):
    """
    Class that splits pages into smaller chunks. This is required because embedding models may not be able to analyze an entire page at once
    """

    def __init__(self, max_tokens_per_section: int = 500):
        self.sentence_endings = STANDARD_SENTENCE_ENDINGS + LATEX_FORMULA_ENDINGS
        self.word_breaks = STANDARD_WORD_BREAKS + LATEX_FORMULA_BREAKS
        self.max_section_length = DEFAULT_SECTION_LENGTH
        self.sentence_search_limit = 100
        self.max_tokens_per_section = max_tokens_per_section
        self.section_overlap = self.max_section_length // DEFAULT_OVERLAP_PERCENT
        self._seen_splits: Set[str] = set()

    def create_split(
        self, page_num: int, text: str, metadata: dict[str, str] | None = None
    ):
        if text in self._seen_splits:
            return PageSplit(page_num=page_num, text="", metadata=metadata)
        self._seen_splits.add(text)
        return PageSplit(page_num=page_num, text=text, metadata=metadata)

    def split_page_by_max_tokens(
        self, page_num: int, text: str, metadata: dict[str, str] | None = None
    ) -> Generator[PageSplit, None, None]:
        """
        Recursively splits page by maximum number of tokens to better handle languages with higher token/word ratios.
        """
        tokens = bpe.encode(text)
        if len(tokens) <= self.max_tokens_per_section:
            # Section is already within max tokens, return
            yield self.create_split(page_num=page_num, text=text, metadata=metadata)
        else:
            # Start from the center and try and find the closest sentence ending by spiralling outward.
            # IF we get to the outer thirds, then just split in half with a 5% overlap
            start = int(len(text) // 2)
            pos = 0
            boundary = int(len(text) // 3)
            split_position = -1
            while start - pos > boundary:
                if text[start - pos] in self.sentence_endings:
                    split_position = start - pos
                    break
                elif text[start + pos] in self.sentence_endings:
                    split_position = start + pos
                    break
                else:
                    pos += 1

            if split_position > 0:
                first_half = text[: split_position + 1]
                second_half = text[split_position + 1 :]
            else:
                # Split page in half and call function again
                # Overlap first and second halves by DEFAULT_OVERLAP_PERCENT%
                middle = int(len(text) // 2)
                overlap = int(len(text) * (DEFAULT_OVERLAP_PERCENT / 100))
                first_half = text[: middle + overlap]
                second_half = text[middle - overlap :]
            yield from self.split_page_by_max_tokens(page_num, first_half)
            yield from self.split_page_by_max_tokens(page_num, second_half)

    def split_pages(self, pages: list[Page]) -> Generator[PageSplit, None, None]:
        def find_page(offset):
            num_pages = len(pages)
            for i in range(num_pages - 1):
                if offset >= pages[i].offset and offset < pages[i + 1].offset:
                    return pages[i]
            return pages[num_pages - 1]

        all_text = "".join(page.text for page in pages)
        if len(all_text.strip()) == 0:
            return

        length = len(all_text)
        if length <= self.max_section_length:
            page0 = find_page(0)
            yield from self.split_page_by_max_tokens(
                page_num=page0.page_num, text=all_text, metadata=page0.metadata
            )
            return

        start = 0
        end = length
        while start + self.section_overlap < length:
            last_word = -1
            end = start + self.max_section_length

            if end > length:
                end = length
            else:
                # Try to find the end of the sentence
                while (
                    end < length
                    and (end - start - self.max_section_length)
                    < self.sentence_search_limit
                    and all_text[end] not in self.sentence_endings
                ):
                    if all_text[end] in self.word_breaks:
                        last_word = end
                    end += 1
                if (
                    end < length
                    and all_text[end] not in self.sentence_endings
                    and last_word > 0
                ):
                    end = last_word  # Fall back to at least keeping a whole word
            if end < length:
                end += 1

            # Try to find the start of the sentence or at least a whole word boundary
            last_word = -1
            while (
                start > 0
                and start
                > end - self.max_section_length - 2 * self.sentence_search_limit
                and all_text[start] not in self.sentence_endings
            ):
                if all_text[start] in self.word_breaks:
                    last_word = start
                start -= 1
            if all_text[start] not in self.sentence_endings and last_word > 0:
                start = last_word
            if start > 0:
                start += 1

            section_text = all_text[start:end]
            page = find_page(start)
            yield from self.split_page_by_max_tokens(
                page_num=page.page_num, text=section_text, metadata=page.metadata
            )

            # a table start at \n| unless |\n| and table end at |\n unless |\n|
            start_matches = list(re.finditer(r"(?<!\|)\n\|", section_text))
            last_table_start = start_matches[-1].start() if start_matches else -1
            end_matches = list(re.finditer(r" \|(?!\n\|)", section_text))
            last_table_end = end_matches[-1].start() + 1 if end_matches else -1
            # last_table_start = section_text.rfind("<table")
            if (
                last_table_start > 2 * self.sentence_search_limit
                and last_table_start > last_table_end
                and last_table_start != -1
                # and last_table_start > section_text.rfind("</table")
            ):
                # If the section ends with an unclosed table, we need to start the next section with the table.
                # If table starts inside sentence_search_limit, we ignore it, as that will cause an infinite loop for tables longer than MAX_SECTION_LENGTH
                # If last table starts inside section_overlap, keep overlapping
                logger.info(
                    f"Section ends with unclosed table, starting next section with the table at page {find_page(start)} offset {start} table start {last_table_start}"
                )
                start = min(end - self.section_overlap, start + last_table_start)
            else:
                start = end - self.section_overlap

        if start + self.section_overlap < end:
            page = find_page(start)
            yield from self.split_page_by_max_tokens(
                page_num=page.page_num, text=all_text[start:end], metadata=page.metadata
            )


class SimpleTextSplitter(TextSplitter):
    """
    Class that splits pages into smaller chunks based on a max object length. It is not aware of the content of the page.
    This is required because embedding models may not be able to analyze an entire page at once
    """

    def __init__(self, max_object_length: int = 1000):
        self.max_object_length = max_object_length

    def split_pages(self, pages: list[Page]) -> Generator[PageSplit, None, None]:
        all_text = "".join(page.text for page in pages)
        if len(all_text.strip()) == 0:
            return

        length = len(all_text)
        if length <= self.max_object_length:
            yield PageSplit(page_num=0, text=all_text)
            return

        # its too big, so we need to split it
        for i in range(0, length, self.max_object_length):
            yield PageSplit(
                page_num=i // self.max_object_length,
                text=all_text[i : i + self.max_object_length],
            )
        return


class SemanticTextSplitter(TextSplitter):
    """
    Class that splits pages into smaller chunks based on the section headers.
    """

    def __init__(
        self,
        max_tokens_per_section: int = 500,
        headers_to_split_on: list[tuple[str, str]] | None = None,
        strip_headers: bool = False,
    ):
        self.text_splitter = SentenceTextSplitter(max_tokens_per_section)
        if headers_to_split_on is None:
            # TODO: experiment with four levels of headers instead of five
            headers_to_split_on = [("#" * i, f"Header {i}") for i in range(1, 6)]
        self.markdown_header_text_splitter = MarkdownHeaderTextSplitter(
            headers_to_split_on=headers_to_split_on, strip_headers=strip_headers
        )

    def split_pages(self, pages: list[Page]) -> Generator[PageSplit, None, None]:
        all_text = "".join(page.text for page in pages)
        if len(all_text.strip()) == 0:
            return
        section_documents = self.markdown_header_text_splitter.split_text(all_text)

        # bind sections text until the text length is greater than MIN_SECTION_LENGTH
        # TODO: think about how to give priority to headers with higher levels
        sections_list: list[PageSplit] = []
        section_text: str = ""
        for section_doc in section_documents:
            section_text += f"\n{cleanup_data(section_doc.page_content)}"
            section_text = section_text.strip()
            if len(section_text) >= DEFAULT_SECTION_LENGTH:
                headers: dict[str, str] = section_doc.metadata
                sections_list.append(PageSplit(text=section_text, metadata=headers))
                section_text = ""
        if section_text:
            metadata = section_doc.metadata
            sections_list.append(PageSplit(text=section_text, metadata=metadata))

        def find_page(offset):
            num_pages = len(pages)
            for i in range(num_pages - 1):
                if offset >= pages[i].offset and offset < pages[i + 1].offset:
                    return pages[i].page_num
            return pages[num_pages - 1].page_num

        # convert each section represented as a PageSplit object to a list of Page objects
        section_offset = 0
        for section in sections_list:
            section_split_pages: list[Page] = []
            section_end = section_offset + len(section.text)
            start_page_num = find_page(section_offset)
            end_page_num = find_page(section_offset + len(section.text))
            text_offset = 0
            for page_num in range(start_page_num, end_page_num + 1):
                page_offset = pages[page_num].offset
                page_end = page_offset + len(pages[page_num].text)
                text_end = min(section_end, page_end) - section_offset
                text = section.text[text_offset:text_end]
                offset = section_offset + text_offset
                metadata = section.metadata
                section_split_pages.append(
                    Page(page_num=page_num, offset=offset, text=text, metadata=metadata)
                )
                text_offset += len(text)
            section_offset += len(section.text)

            yield from self.text_splitter.split_pages(section_split_pages)
