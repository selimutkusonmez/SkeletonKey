from abc import ABC,abstractmethod

class BaseCipher(ABC):

    @staticmethod
    @abstractmethod
    def encrypt(text,key):
        pass

    @staticmethod
    @abstractmethod
    def decrypt(text,key):
        pass