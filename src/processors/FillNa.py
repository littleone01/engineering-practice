from typing import List

from pandas import DataFrame

from src.processors.ProcessorBase import ProcessorBase


class FillNa(ProcessorBase):
    def __init__(self, fill_value: object):
        self.fill_value =fill_value

    def process(self, data: DataFrame, process_fields: List[str] = []) -> DataFrame:
        data[process_fields] = data[process_fields].fillna(value=self.fill_value)
        return data