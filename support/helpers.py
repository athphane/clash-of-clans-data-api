import os


def get_cache_file_name(file_name: str, table: str) -> str:
    return f"cache/{file_name}-{table}.csv"


def check_for_cache(file_name, table: str) -> bool:
    return os.path.exists(get_cache_file_name(file_name, table))
