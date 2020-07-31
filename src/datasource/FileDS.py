
from typing import List

from pandas import DataFrame
import pandas as pd

from src.datasource.DataSourceBase import DataSourceBase
from src.exception.FileTypeNotSupportError import FileTypeNotSupportError

DB_NAME = 'file_db'


class FileDS(DataSourceBase):
    def __init__(self):
        super(FileDS, self).__init__(DB_NAME)

    def get_data(self, file_name: str, file_type: str, indexes: List[str] = None) -> DataFrame:
        if file_type == 'excel':
            return pd.read_excel(file_name)
        elif file_type == 'csv':
            return pd.read_csv(file_name)
        else:
            raise FileTypeNotSupportError(f'not support file type: {file_type}')


if __name__ == '__main__':
    data = FileDS().get_data([])
    print(data)
