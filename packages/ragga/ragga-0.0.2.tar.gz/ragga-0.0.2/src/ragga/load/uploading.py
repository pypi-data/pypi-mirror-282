# ragga/load/uploading.py
from llama_index.core import SimpleDirectoryReader


def upload(directory_path: str):
    """
    Upload data from the specified directory using SimpleDirectoryReader.

    :param directory_path: Path to the directory containing data.
    :return: Loaded data.
    """
    reader = SimpleDirectoryReader(directory_path)
    return reader.load_data(num_workers=5)
