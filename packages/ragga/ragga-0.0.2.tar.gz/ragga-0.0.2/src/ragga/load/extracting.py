# ragga/load/extracting.py
from llama_index.core.extractors import KeywordExtractor


def extract_keyword(documents, keywords=10):
    """
    Extract keyword from the documents using KeywordExtractor.

    :param documents: The documents to extract entities from.
    :return: Documents with extracted entities.
    """
    keyword_extractor = KeywordExtractor(
        keywords=keywords,
    )
    return [keyword_extractor.extract(document) for document in documents]
