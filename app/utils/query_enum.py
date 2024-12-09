from enum import Enum


class QueryEnum(Enum):

    GET_ALL_TABLES = "SELECT name FROM sqlite_master where type='table'"
    GET_TABLE_SCHEMA = "PRAGMA table_info('{table}')"
    GET_RECORDS = "SELECT * from {table}"

