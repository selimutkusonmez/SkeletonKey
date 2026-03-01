from .base_cipher import BaseCipher

class VigenereAlgorithm(BaseCipher):

    @staticmethod
    def encrypt(text, key):
        return super().encrypt(text, key)
    
    @staticmethod
    def decrypt(text, key):
        return super().decrypt(text, key)