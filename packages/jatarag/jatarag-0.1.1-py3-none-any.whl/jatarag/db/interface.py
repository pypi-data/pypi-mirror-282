from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Result(ABC):
    score: float  # should be a value from 0 to 1

    @abstractmethod
    def get_id(self) -> str:
        """return a unique identifier for the content this result corresponds to"""

    def __post_init__(self):
        if self.score < 0 or self.score > 1:
            raise ValueError(f"score must be between 0 and 1, got {self.score}")


@dataclass
class Paragraph:
    document_id: str
    paragraph_idx: int
    paragraph: str


@dataclass
class Metadata:
    document_id: str
    title: str
    author: str
    publisher: str


@dataclass
class ParagraphResult(Result, Paragraph):
    def get_id(self) -> str:
        return f'{self.document_id}-{self.paragraph_idx}'


@dataclass
class MetadataResult(Result, Metadata):
    def get_id(self) -> str:
        return self.document_id


class Database(ABC):
    # TODO: long-term, would love to be able to omit some methods (e.g. if metadata wasn't available), and dynamically update the llm prompt to not mention them

    ######################## data methods ########################
    # TBD if these are needed in the interface
    # @abstractmethod
    # def get_document_metadata(self, document_id: str) -> MetadataResult:
    #     """given a document id, return its metadata"""

    # @abstractmethod
    # def get_document_paragraphs(self, document_id: str) -> list[str]:
    #     """given a document id, return a list of its paragraphs"""

    ######################## query methods ########################
    @abstractmethod
    def query_all_documents(self, query: str, max_results: int = 10) -> list[ParagraphResult]:
        """perform a search over all document paragraphs in the database for the given query"""

    @abstractmethod
    def query_single_document(self, document_id: str, query: str, max_results: int = 10) -> list[ParagraphResult]:
        """perform a search over a single document in the database for the given query"""

    @abstractmethod
    def query_titles(self, query: str, max_results: int = 10) -> list[MetadataResult]:
        """perform a search over all document titles in the database for the given query"""

    @abstractmethod
    def query_authors(self, author: str, max_results: int = 10) -> list[MetadataResult]:
        """perform a search over all document authors in the database for the given query"""

    @abstractmethod
    def query_publishers(self, publisher: str, max_results: int = 10) -> list[MetadataResult]:
        """perform a search over all document publishers in the database for the given query"""


def reciprocal_rank_fusion(results: list[list[Result]]) -> list[Result]:
    """
    Combines multiple lists of results using the Reciprocal Rank Fusion method

    This can be used in concrete implementations of the Database interface to
    allow more advanced search strategies by combining multiple search methods.
    For example, you could combine a semantic search + keyword search over
    document paragraphs, or phonetic search + fuzzy search over author names.

    Parameters:
        results (list[list[Result]]): a list of result lists to be fused.

    Returns:
        list[Result]: a fused list of results
    """
    raise NotImplementedError
