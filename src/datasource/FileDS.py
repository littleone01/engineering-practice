from pandas import DataFrame
import pandas as pd

from src.datasource.DataSourceBase import DataSourceBase
from src.exception.TypeNotSupportError import TypeNotSupportError
from src.entity.FileType import FileType

DB_NAME = 'file_db'


class FileDS(DataSourceBase):
    def __init__(self, file_name: str, file_type: FileType):
        super(FileDS, self).__init__(DB_NAME)
        self.file_name = file_name
        self.file_type = file_type

    def get_data(self, sql: str) -> DataFrame:
        if self.file_type == FileType.EXCEL:
            return pd.read_excel(self.file_name)
        elif self.file_type == FileType.CSV:
            return pd.read_csv(self.file_name)
        else:
            raise TypeNotSupportError(f'not support file type: {self.file_type}')

    def write_data(self, file_dir: str, data: DataFrame):
        import os
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)
        data.to_csv(os.path.join(file_dir, self.file_name))

    def execute(self, sql: str):
        pass

