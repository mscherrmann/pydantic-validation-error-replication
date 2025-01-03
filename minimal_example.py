from zenml import pipeline, step

from evaluation.schema import Chunk, RetrievalCorpus, RetrievalCorpusCollection


@step
def producer() -> RetrievalCorpus:
    return RetrievalCorpus(
        chunks={
            "chunk_id": Chunk(
                text="text",
                chunk_type="document_chunk",
                document_id="document_id",
                page_n=1,
                retrieval_text="retrieval_text",
                title="title",
            )
        },
        queries={"query_id": "query"},
        query_chunk_map={"query_id": {"chunk_id": 1}},
        answers={"query_id": "answer"},
    )


@step()
def consumer(input_: RetrievalCorpus | RetrievalCorpusCollection) -> None:
    pass


@pipeline(enable_cache=False)
def p():
    consumer(producer())


if __name__ == "__main__":
    p()
