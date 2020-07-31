from abc import abstractmethod

from src.utils.read_config import ConfigReader


class DataSourceBase:
    def __init__(self, ds_name):
        self.ds_config = ConfigReader().get_ds_config(ds_name)

    @abstractmethod
    def execute(self, sql: str):
        pass
