from dataclasses import dataclass, asdict


@dataclass(kw_only=True, frozen=True, slots=True)
class DocSplit:
    """A section of a document that has been split into a smaller chunk."""

    page_num: int = 0

    def as_dict(self):
        return asdict(self)
    
    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)


@dataclass(kw_only=True, frozen=True, slots=True)
class Page(DocSplit):
    """A single page from a document"""

    # OFFSET: If the text of the entire Document was concatenated into a single str, the index of the first character on the page.
    # For example, if page 1 had the text "hello" and page 2 had the text "world", the offset of page 2 is 5 ("hellow")
    offset: int
    text: str
    metadata: dict[str, str] | None = None


@dataclass(kw_only=True, frozen=True, slots=True)
class PageSplit(DocSplit):
    """A section of a page that has been split into a smaller chunk."""

    text: str
    metadata: dict[str, str] | None = None


@dataclass(kw_only=True, frozen=True, slots=True)
class PageFigure(DocSplit):
    """A figure from a page"""

    fig_num: int  # The figure number on the page
    coords: tuple[float, float]  # The y0 and y1 coordinates of the figure on the page
    caption: str
