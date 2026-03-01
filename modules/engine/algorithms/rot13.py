from .base_cipher import BaseCipher

class Rot13Algorithm(BaseCipher):
    @staticmethod
    def _shift(text: str) -> str:
        """Core math for shifting alphabetical characters by exactly 13."""
        alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
        alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        output = []
        
        for char in text:
            if char in alphabet_lower:
                new_index = (alphabet_lower.index(char) + 13) % 26
                output.append(alphabet_lower[new_index])
            elif char in alphabet_upper:
                new_index = (alphabet_upper.index(char) + 13) % 26
                output.append(alphabet_upper[new_index])
            else:
                output.append(char)
                
        return "".join(output)

    @staticmethod
    def encrypt(text: str, key: str) -> str:
        return Rot13Algorithm._shift(text)
    
    @staticmethod
    def decrypt(text: str, key: str) -> str:
        return Rot13Algorithm._shift(text)