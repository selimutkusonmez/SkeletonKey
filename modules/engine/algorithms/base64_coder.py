from .base_coder import BaseCoder

class Base64(BaseCoder):

    @staticmethod
    def encode(text):
        return super().encode(text)
    
    @staticmethod
    def decode(text):
        return super().decode(text)