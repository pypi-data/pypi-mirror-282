# ragga/load/chunking.py
from llama_index.core.node_parser import SentenceSplitter


def chunk(documents, chunk_size=512, chunk_overlap=20):
    """
    Chunk the data into smaller pieces using SentenceSplitter.

    :param documents: The documents to be chunked.
    :param chunk_size: The size of each chunk.
    :param chunk_overlap: The overlap size between chunks.
    :return: A list of data chunks.
    """
    splitter = SentenceSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return splitter.get_nodes_from_documents(documents)
