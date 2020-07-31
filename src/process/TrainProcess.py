from src.process.ProcessBase import ProcessBase


class TrainProcess(ProcessBase):
    def __init__(self):
        super(TrainProcess, self).__init__('train')

    def run(self):
        print('train')