from abc import ABC,abstractmethod

class BaseCoder(ABC):

    @staticmethod
    @abstractmethod
    def encode(text):
        pass

    @staticmethod
    @abstractmethod
    def decode(text):
        pass
