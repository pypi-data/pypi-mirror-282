import re
from typing import IO, AsyncGenerator

from .doc_split import Page


def cleanup_data(data: str) -> str:
    """Cleans up the given content using regexes
    Args:
        data: (str): The data to clean up.
    Returns:
        str: The cleaned up data.
    """
    # match two or more newlines and replace them with one new line
    output = re.sub(r"\n{2,}", "\n", data)
    # match two or more spaces that are not newlines and replace them with one space
    output = re.sub(r"[^\S\n]{2,}", " ", output)

    return output.strip()


class TextParser:
    """Parses simple text into a Page object."""

    async def parse(self, content: IO) -> AsyncGenerator[Page, None]:
        data = content.read()
        decoded_data = data.decode("utf-8")
        text = cleanup_data(decoded_data)
        yield Page(page_num=0, offset=0, text=text)
