import os
from typing import Tuple, List

from pandas import DataFrame

from src.datasource.DataSourceBase import DataSourceBase
from cx_Oracle import connect, makedsn

os.environ["NLS_LANG"] = "AMERICAN_AMERICA.AL32UTF8"
DB_NAME = 'oracle_db'


class OracleDS(DataSourceBase):
    def __init__(self):
        super(OracleDS, self).__init__(DB_NAME)

    def get_data(self, sql: str) -> DataFrame:
        import pandas as pd

        with connect(
                self.ds_config['username'],
                self.ds_config['password'],
                # makedsn(self.ds_config['hostname'], self.ds_config['port'], self.ds_config['service'],
                self.ds_config['hostname']
        ) as connection:
            return pd.read_sql(sql, connection)

    def execute(self, sql: str):
        with connect(
                self.ds_config['username'],
                self.ds_config['password'],
                # makedsn(self.ds_config['hostname'], self.ds_config['port'], self.ds_config['service'],
                self.ds_config['hostname']
        ) as connection:
            cursor = connection.cursor()
            cursor.execute(sql)
            connection.commit()

    def execute_many(self, sql: str, data: List[Tuple]):
        with connect(
                self.ds_config['username'],
                self.ds_config['password'],
                # makedsn(self.ds_config['hostname'], self.ds_config['port'], self.ds_config['service'],
                self.ds_config['hostname']
        ) as connection:
            cursor = connection.cursor()
            cursor.executemany(sql, data)
            connection.commit()