# ragga/load/load.py
from .uploading import upload
from .chunking import chunk
from .extracting import extract_keyword


def load(directory_path: str, chunk_size=1024, chunk_overlap=20, keywords=10):
    """
    Load data from the specified directory, chunk it using SentenceSplitter, and extract entities using EntityExtractor.

    :param directory_path: Path to the directory containing data.
    :param chunk_size: The size of each chunk.
    :param chunk_overlap: The overlap size between chunks.
    :return: A list of data chunks with extracted entities.
    """
    documents = upload(directory_path)
    chunks = chunk(documents, chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return extract_keyword(
        chunks,
        keywords=keywords,
    )
