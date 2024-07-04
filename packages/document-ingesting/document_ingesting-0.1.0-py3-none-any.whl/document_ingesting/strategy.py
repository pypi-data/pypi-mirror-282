from abc import ABC
from enum import Enum


class DocumentAction(str, Enum):
    add = "add"
    remove = "remove"
    remove_all = "removeall"


class Strategy(ABC):
    """
    Abstract strategy for ingesting documents into a search service. It has a single setup 
    step to perform any required initialization, and then a run step that actually ingests 
    documents into the search service.
    """

    async def setup(self):
        raise NotImplementedError

    async def run(self):
        raise NotImplementedError
