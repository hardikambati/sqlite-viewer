from fastapi import HTTPException

from db import DBConnector
from utils.query_enum import QueryEnum


class DBService:
    def __init__(self):
        """Constructor"""
        self.db_instance = DBConnector()
        self.cursor = self.db_instance.connect()

    def __del__(self):
        """Destructor"""
        self.db_instance.disconnect()
        
    def get_all_tables(self) -> list:
        # [('users',), ('orders',)]
        try:
            self.cursor.execute(QueryEnum.GET_ALL_TABLES.value)
            tables: list = self.cursor.fetchall()
            data = [table[0] for table in tables]
            return data
        except Exception as e:
            print(e)
            return []

    def get_column_names(self, name: str) -> list:
        # [
        #   (0, 'id', 'INTEGER', 0, None, 1),
        #   (1, 'username', 'VARCHAR', 0, None, 0),
        #   (2, 'email', 'VARCHAR', 0, None, 0),
        #   (3, 'hashed_password', 'VARCHAR', 0, None, 0)
        # ]
        self.cursor.execute(QueryEnum.GET_TABLE_SCHEMA.value.format(table=name))
        schema: list = self.cursor.fetchall()
        schema = [col[1] for col in schema]
        return schema

    def get_records_for_table(self, name: str) -> list:
        # [(1, 'tes1', 'test1@example.com', '$2b$12$Ek1zMn1rJSlsjYVTLBYmd.BeiHRikR7/NcW6KIcQUqAzZViR2Nj/.'),]
        try:
            self.cursor.execute(QueryEnum.GET_RECORDS.value.format(table=name))
            records: list = self.cursor.fetchall()
            return records
        except Exception as e:
            raise HTTPException(detail=f"Table with name {name} does not exist", status_code=400)