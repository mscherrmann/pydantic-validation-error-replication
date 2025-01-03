from typing import Literal, Optional, TypeAlias

from pydantic import BaseModel


# Define the basic structure of a chunk
class Chunk(BaseModel):
    text: str
    chunk_type: Literal["document_chunk", "data_room_field"] = "document_chunk"
    document_id: Optional[str] = None
    page_n: Optional[int] = None
    retrieval_text: Optional[str] = None
    title: Optional[str] = None

    def to_dict(self, for_retrieval: bool = False) -> dict[str, str]:
        return {
            "text": self.retrieval_text if for_retrieval and self.retrieval_text else self.text,
            "chunk_type": self.chunk_type,
            "document_id": self.document_id if self.document_id else "",
            "page_n": str(self.page_n) if self.page_n else "",
            "title": self.title if self.title else "",
        }


# Type aliases with docstrings
Chunks: TypeAlias = dict[str, Chunk]
"""Mapping of chunk IDs to Chunk objects"""

Queries: TypeAlias = dict[str, str]
"""Mapping of query IDs to query strings"""

Answers: TypeAlias = dict[str, str]
"""Mapping of query IDs to answer strings"""

QueryChunkMap: TypeAlias = dict[str, dict[str, int | float]]
"""Mapping of query IDs to dictionaries mapping chunk IDs to relevance scores"""


# Define the structure of a dataset split
class RetrievalCorpus(BaseModel):
    chunks: Chunks
    queries: Queries
    query_chunk_map: QueryChunkMap
    answers: Optional[Answers] = None

    def is_empty(self) -> bool:
        return (
            not self.chunks
            and not self.queries
            and not self.query_chunk_map
            and (self.answers is None or not self.answers)
        )


RetrievalCorpusCollection: TypeAlias = dict[str, RetrievalCorpus]
"""Mapping of dataset groups to RetrievalCorpus objects"""
