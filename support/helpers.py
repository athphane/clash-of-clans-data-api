import os

from app.enums import TableType


def get_cache_file_name(file_name: str, table: str) -> str:
    """
    Generates a cache file name based on the provided file name and table.

    :param file_name:
    :param table:
    :return:
    """
    return f"cache/{file_name}-{table}.csv"


def check_for_cache(file_name, table: str) -> bool:
    """
    Checks if a cache file exists for the given file name and table.

    :param file_name:
    :param table:
    :return:
    """
    return os.path.exists(get_cache_file_name(file_name, table))
