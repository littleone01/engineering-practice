from abc import abstractmethod


class ProcessBase:
    def __init__(self, process_name):
        self.process_name = process_name

    @abstractmethod
    def run(self):
        pass
