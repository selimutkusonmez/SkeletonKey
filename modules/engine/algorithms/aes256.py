import os
import hashlib
import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from .base_cipher import BaseCipher

class Aes256Algorithm(BaseCipher):

    @staticmethod
    def _get_32_byte_key(key_input: str) -> bytes:
        clean_key = key_input.strip()
        if len(clean_key) == 64:
            try:
                return bytes.fromhex(clean_key)
            except ValueError:
                pass 
        return hashlib.sha256(key_input.encode('utf-8')).digest()

    @staticmethod
    def encrypt(text: str, key: str) -> str:
        try:
            aes_key = Aes256Algorithm._get_32_byte_key(key)
            iv = os.urandom(16)
            
            padder = padding.PKCS7(128).padder()
            padded_data = padder.update(text.encode('utf-8')) + padder.finalize()
            
            cipher = Cipher(algorithms.AES(aes_key), modes.CBC(iv), backend=default_backend())
            encryptor = cipher.encryptor()
            ciphertext = encryptor.update(padded_data) + encryptor.finalize()
            
            final_package = iv + ciphertext
            output_text = base64.b64encode(final_package).decode('utf-8')
            
            # Append the hex-encoded key to the output
            return f"{output_text}\n\nHashed Key : {aes_key.hex()}"
            
        except Exception as e:
            return f"Error: Encryption failed. ({str(e)})"
    
    @staticmethod
    def decrypt(text: str, key: str) -> str:
        try:
            raw_package = base64.b64decode(text.strip())
            
            iv = raw_package[:16]
            ciphertext = raw_package[16:]
            
            aes_key = Aes256Algorithm._get_32_byte_key(key)
            cipher = Cipher(algorithms.AES(aes_key), modes.CBC(iv), backend=default_backend())
            decryptor = cipher.decryptor()
            padded_data = decryptor.update(ciphertext) + decryptor.finalize()
            
            unpadder = padding.PKCS7(128).unpadder()
            original_bytes = unpadder.update(padded_data) + unpadder.finalize()
            
            output_text = original_bytes.decode('utf-8')
            
            # Append the hex-encoded key to the output
            return f"{output_text}"
            
        except Exception:
            return "Error: Decryption failed. Invalid key, corrupted data, or wrong format."