import pandas
from pandas import DataFrame
from mysql.connector import connect

from src.datasource.DataSourceBase import DataSourceBase

DB_NAME = 'mysql_db'


class MysqlDS(DataSourceBase):
    def __init__(self, db: str):
        super(MysqlDS, self).__init__(DB_NAME)
        self.db = db

    def execute(self, sql: str):
        with connect(host=self.ds_config['host'],
                     user=self.ds_config['username'],
                     password=self.ds_config['password'],
                     database=self.ds_config['db']) as connection:
            cursor = connection.cursor()
            cursor.execute(sql)

    def get_data(self, sql: str) -> DataFrame:
        with connect(host=self.ds_config['host'],
                     user=self.ds_config['username'],
                     password=self.ds_config['password'],
                     database=self.db) as connection:
            return pandas.read_sql(sql, connection)
