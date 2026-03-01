from .base_cipher import BaseCipher

class XorAlgorithm(BaseCipher):

    @staticmethod
    def _process(text_bytes: bytes, key_bytes: bytes) -> bytes:
        """Core math for XOR bitwise operations."""
        output = bytearray()
        key_length = len(key_bytes)
        
        for i in range(len(text_bytes)):
            xored_byte = text_bytes[i] ^ key_bytes[i % key_length]
            output.append(xored_byte)
            
        return bytes(output)

    @staticmethod
    def encrypt(text: str, key: str) -> str:
        text_bytes = text.encode('utf-8')
        key_bytes = key.encode('utf-8')
        
        scrambled_bytes = XorAlgorithm._process(text_bytes, key_bytes)
        
        return scrambled_bytes.hex()
    
    @staticmethod
    def decrypt(text: str, key: str) -> str:
        try:
            text_bytes = bytes.fromhex(text.strip())
        except ValueError:
            return "Error: XOR decryption requires a valid hexadecimal string."
            
        key_bytes = key.encode('utf-8')
        
        unscrambled_bytes = XorAlgorithm._process(text_bytes, key_bytes)
        
        try:
            return unscrambled_bytes.decode('utf-8')
        except UnicodeDecodeError:
            return "Error: Invalid key or corrupted data. Cannot decode to UTF-8."