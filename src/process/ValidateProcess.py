from src.process.ProcessBase import ProcessBase


class ValidateProcess(ProcessBase):
    def __init__(self):
        super(ValidateProcess, self).__init__('validate')

    def run(self):
        print('validate')