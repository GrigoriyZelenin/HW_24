from typing import Optional, Callable

import funcions

CMD_TO_FUNCTION: dict[str, Callable] = {
    'filter': funcions.filter_query,
    'map': funcions.map_query,
    'unique': funcions.unique_query,
    'sort': funcions.sort_query,
    'limit': funcions.limit_query,
    "regex": funcions.regex_query
}

FILE_NAME: str = 'data/apache_logs.txt'


def build_query(cmd: str, param: str, data: Optional[list[str]]) -> list[str]:
    if data is None:
        with open(FILE_NAME) as file:
            prepared_data: list[str] = list(map(lambda x: x.strip(), file))

    else:
        prepared_data = data

        return CMD_TO_FUNCTION[cmd](param=param, data=prepared_data)