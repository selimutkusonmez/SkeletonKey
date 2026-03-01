from .base_hasher import BaseHasher

class AesAlgorithm(BaseHasher):

    @staticmethod
    def hash(text):
        return super().hash(text)