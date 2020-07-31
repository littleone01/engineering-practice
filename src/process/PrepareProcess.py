from src.process.ProcessBase import ProcessBase


class PrepareProcess(ProcessBase):
    def __init__(self):
        super(PrepareProcess, self).__init__('prepare')

    def run(self):
        print('prepare')