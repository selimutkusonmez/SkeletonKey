from .base_cipher import BaseCipher

class Aes256Algorithm(BaseCipher):

    @staticmethod
    def encrypt(text, key):
        return super().encrypt(text, key)
    
    @staticmethod
    def decrypt(text, key):
        return super().decrypt(text, key)