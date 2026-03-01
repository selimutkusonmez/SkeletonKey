import base64
from .base_cipher import BaseCipher

class Base64(BaseCipher):

    @staticmethod
    def encode(text: str) -> str:
        try:
            raw_bytes = text.encode('utf-8')
            encoded_bytes = base64.b64encode(raw_bytes)
            return encoded_bytes.decode('utf-8')
        except Exception as e:
            return f"Error: Encoding failed. ({str(e)})"
    
    @staticmethod
    def decode(text: str) -> str:
        try:
            decoded_bytes = base64.b64decode(text.strip())
            return decoded_bytes.decode('utf-8')
        except Exception:
            return "Error: Decoding failed. Invalid Base64 string or corrupted data."