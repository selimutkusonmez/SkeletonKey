from .base_cipher import BaseCipher

class AtbashAlgorithm(BaseCipher):

    @staticmethod
    def _process(text: str) -> str:
        """Core math for flipping alphabetical characters."""
        alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
        alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        output = []
        
        for char in text:
            if char in alphabet_lower:
                new_index = 25 - alphabet_lower.index(char)
                output.append(alphabet_lower[new_index])
            elif char in alphabet_upper:
                new_index = 25 - alphabet_upper.index(char)
                output.append(alphabet_upper[new_index])
            else:
                output.append(char)
                
        return "".join(output)

    @staticmethod
    def encrypt(text: str, key: str) -> str:
        return AtbashAlgorithm._process(text)
    
    @staticmethod
    def decrypt(text: str, key: str) -> str:
        return AtbashAlgorithm._process(text)