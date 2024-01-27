from abc import ABC, abstractmethod

class ApiInterface(ABC):
    @abstractmethod
    def submit(self, data):
        pass