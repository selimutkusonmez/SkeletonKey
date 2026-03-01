from .base_cipher import BaseCipher

class CaesarAlgorithm(BaseCipher):

    @staticmethod
    def _shift(text: str, shift: int) -> str:
        """Core math for shifting alphabetical characters."""
        alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
        alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        output = []
        
        for char in text:
            if char in alphabet_lower:
                new_index = (alphabet_lower.index(char) + shift) % 26
                output.append(alphabet_lower[new_index])
            elif char in alphabet_upper:
                new_index = (alphabet_upper.index(char) + shift) % 26
                output.append(alphabet_upper[new_index])
            else:
                output.append(char)
                
        return "".join(output)

    @staticmethod
    def encrypt(text: str, key: str) -> str:
        try:
            shift = int(key)
        except ValueError:
            return "Error: Caesar cipher key must be an integer."
            
        return CaesarAlgorithm._shift(text, shift)
    
    @staticmethod
    def decrypt(text: str, key: str) -> str:
        try:
            shift = int(key)
        except ValueError:
            return "Error: Caesar cipher key must be an integer."
            
        return CaesarAlgorithm._shift(text, -shift)