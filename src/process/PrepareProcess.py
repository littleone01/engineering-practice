from typing import List

from src.datasource import DataSourceBase
from src.process.ProcessBase import ProcessBase

from src.processors.ProcessorBase import ProcessorBase


class PrepareProcess(ProcessBase):
    def __init__(self, ds: DataSourceBase, preprocessors: List[ProcessorBase], save_name: str):
        super(PrepareProcess, self).__init__('prepare')
        self.ds = ds
        self.preprocessors = preprocessors
        self.save_name = save_name

    def run(self):
        from src.utils.process_dirs import prepared_file_dir
        from src.utils.sql_utils import get_credit_info_sql
        data = self.ds.get_data(get_credit_info_sql)
        result = None
        for processor in self.preprocessors:
            result = processor.process(data, data.columns.tolist())

        from src.datasource.FileDS import FileDS
        from src.entity.FileType import FileType
        file_ds = FileDS(self.save_name, FileType.CSV)
        file_ds.write_data(prepared_file_dir, result)


