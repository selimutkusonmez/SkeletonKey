from abc import ABC,abstractmethod

class BaseHasher(ABC):

    @staticmethod
    @abstractmethod
    def hash(text):
        pass
