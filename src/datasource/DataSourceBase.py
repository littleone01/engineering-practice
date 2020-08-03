from abc import abstractmethod

from pandas import DataFrame

from src.utils.ReadConfig import ConfigReader


class DataSourceBase:
    def __init__(self, ds_name):
        self.ds_config = ConfigReader().get_ds_config(ds_name)

    @abstractmethod
    def execute(self, sql: str):
        pass

    @abstractmethod
    def get_data(self, sql: str) -> DataFrame:
        pass
