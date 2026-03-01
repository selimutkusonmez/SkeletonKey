from .base_hasher import BaseHasher

class Sha256Hasher(BaseHasher):

    @staticmethod
    def hash(text):
        return super().hash(text)