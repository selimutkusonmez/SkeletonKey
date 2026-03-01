from .base_cipher import BaseCipher

class VigenereAlgorithm(BaseCipher):

    @staticmethod
    def _process(text: str, key: str, mode: str) -> str:
        """Core math for Vigenère shifting using a keyword."""
        if not key.isalpha():
            return "Error: Vigenère key must contain only alphabetic letters."
        
        key = key.lower()
        key_length = len(key)
        key_index = 0
        output = []

        alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
        alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        for char in text:
            if char in alphabet_lower:
                shift = alphabet_lower.index(key[key_index % key_length])
                if mode == "decrypt":
                    shift = -shift
                
                new_index = (alphabet_lower.index(char) + shift) % 26
                output.append(alphabet_lower[new_index])
                key_index += 1
                
            elif char in alphabet_upper:
                shift = alphabet_lower.index(key[key_index % key_length])
                if mode == "decrypt":
                    shift = -shift
                    
                new_index = (alphabet_upper.index(char) + shift) % 26
                output.append(alphabet_upper[new_index])
                key_index += 1
                
            else:
                output.append(char)
                
        return "".join(output)

    @staticmethod
    def encrypt(text: str, key: str) -> str:
        return VigenereAlgorithm._process(text, key, "encrypt")
    
    @staticmethod
    def decrypt(text: str, key: str) -> str:
        return VigenereAlgorithm._process(text, key, "decrypt")