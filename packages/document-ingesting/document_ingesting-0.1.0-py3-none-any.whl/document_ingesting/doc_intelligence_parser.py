import logging
import re


from document_ingesting.azure_helper.doc_intelligence_lite import (
    AnalyzeResultLite,
    DocFormula,
    DocPage,
)

from .doc_split import Page, PageFigure

logger = logging.getLogger("ingester")

# TODO: research why there are a lot of "//" in the resultant chunks


def cleanup_data(data: str) -> str:
    """Cleans up the given content using regexes and string replacements."""
    # remove the comments
    data = re.sub(r"<!--.*?-->", "", data, flags=re.DOTALL)
    # remove the formula tags
    data = data.replace(":formula:", "")
    data = re.sub(r"(?<=\$)( *\n*)formula:(?= )", r"\1", data)
    # remove selection marks tags
    data = data.replace(":selected:", "")
    data = data.replace(":unselected:", "")
    # match all lines with only whitespaces and replace them with empty string.
    data = re.sub(r"^\s+$", "", data, flags=re.MULTILINE)
    # match two or more newlines and replace them with one new lines
    data = re.sub(r"\n{2,}", "\n", data)
    # match two or more spaces that are not newlines and replace them with one space
    data = re.sub(r"[^\S\n]{2,}", " ", data)
    # remove leading and trailing whitespaces from each line
    data = "\n".join(line.strip() for line in data.splitlines())
    # correct to normal text the headers that are table captions
    data = re.sub(r"\n#+ Table", "\nTable", data)
    return data.strip()


class DocIntelligenceParser:
    """
    Concrete parser backed by Azure AI Document Intelligence that can parse many document formats into pages
    To learn more, please visit https://learn.microsoft.com/azure/ai-services/document-intelligence/overview
    """

    def __init__(self):
        pass

    async def parse(self, filepath: str):
        """Parses the given file into pages"""
        analysis_results = AnalyzeResultLite.from_json(filepath)
        for page in self.parse_analysis(analysis=analysis_results):
            yield page

    def parse_analysis(self, analysis: AnalyzeResultLite):
        """Formats the document analysis result into pages"""
        cum_page_offset = 0  # offset each page in the doc after modifications
        doc_content = analysis.content
        for page_num, page in enumerate(analysis.pages):
            # extract the content of the page
            page_offset = page.span.offset
            page_end = page_offset + page.span.length
            page_content = doc_content[page_offset:page_end]
            if page.formulas:  # embed the formulas in the content
                page_content = DocIntelligenceParser.embed_formulas(
                    page=page, content=page_content
                )
            page_content = cleanup_data(data=page_content)
            yield Page(page_num=page_num, offset=cum_page_offset, text=page_content)
            cum_page_offset += len(page_content)

    def get_parsed_analysis(self, analysis: AnalyzeResultLite):
        return [page for page in self.parse_analysis(analysis)]

    @staticmethod
    def embed_formulas(page: DocPage, content: str):
        """Embeds the formulas into the content of the page"""
        if not page.formulas:
            return content

        page_offset = page.span.offset
        page_items = page.formulas + (page.words or [])
        page_items = sorted(page_items, key=lambda x: x.sort_index)

        cum_added_length = 0
        next_offset = 0
        for item in page_items:
            if isinstance(item, DocFormula):
                # extract formula content with the appropriate separator
                separator_str = "\n\n$$" if item.kind == "display" else " $"
                formula_content = separator_str + item.value + separator_str[::-1]
                # insert formula in the current item offset and update iter variables
                content = (
                    f"{content[:next_offset]}{formula_content}{content[next_offset:]}"
                )
                next_offset = next_offset + len(formula_content)
                cum_added_length += len(formula_content)
            else:  # if word only save offset for next item
                item_offset = item.span.offset - page_offset + cum_added_length
                next_offset = item_offset + item.span.length
        return content
