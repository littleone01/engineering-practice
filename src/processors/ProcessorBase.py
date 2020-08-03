from abc import abstractmethod
from typing import List

from pandas import DataFrame


class ProcessorBase:
    @abstractmethod
    def process(self, data: DataFrame, process_fields: List[str] = []) -> DataFrame:
        pass