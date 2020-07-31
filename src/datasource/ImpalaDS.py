import pandas
from pyhive.hive import Connection
from pandas import DataFrame

from src.datasource.DataSourceBase import DataSourceBase

DB_NAME = 'impala_db'


class ImpalaDS(DataSourceBase):
    def __init__(self):
        super(ImpalaDS, self).__init__(DB_NAME)

    def get_data(self, sql: str) -> DataFrame:
        with Connection(host=self.ds_config['host'], port=int(self.ds_config['port']),
                        database=self.ds_config['database'], username=self.ds_config['user'],
                        password=self.ds_config['password'], auth='CUSTOM') as connection:
            return pandas.read_sql(sql, connection)

    def execute(self, sql: str):
        with Connection(host=self.ds_config['host'], port=int(self.ds_config['port']),
                        database=self.ds_config['database'], username=self.ds_config['user'],
                        password=self.ds_config['password'], auth='CUSTOM') as connection:
            cursor = connection.cursor()
            cursor.execute(sql)
