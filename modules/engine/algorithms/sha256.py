import hashlib
from .base_cipher import BaseCipher

class Sha256Hasher(BaseCipher):

    @staticmethod
    def hash(text: str) -> str:
        try:
            raw_bytes = text.encode('utf-8')
            hashed_bytes = hashlib.sha256(raw_bytes).digest()
            return hashed_bytes.hex()
        except Exception as e:
            return f"Error: Hashing failed. ({str(e)})"
    
