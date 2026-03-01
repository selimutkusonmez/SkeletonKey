from modules.engine.algorithms import *

class CipherEngine():
    def __init__(self):
        self.algorithm_map = {
            "Caesar": CaesarAlgorithm,
            "Vigenère": VigenereAlgorithm,
            "ROT13": Rot13Algorithm,
            "Atbash": AtbashAlgorithm,
            "XOR": XorAlgorithm,
            "AES-256": Aes256Algorithm,
            "DES": DesAlgorithm,
            "Blowfish": BlowfishAlgorithm,
            "RSA": RsaAlgorithm,
            "Base64": Base64,
            "SHA-256": Sha256Hasher
        }

    def cipher(self,key,algorithm,mode,input_text):

        worker_class = self.algorithm_map.get(algorithm)

        if algorithm == "SHA-256":
            return worker_class.hash(input_text)
            
        elif algorithm == "Base64":
            if mode == "Encode":
                return worker_class.encode(input_text)
            elif mode == "Decode":
                return worker_class.decode(input_text)
            
        elif mode == "Encrypt":
            return worker_class.encrypt(key,input_text)
        
        elif mode == "Decrypt":
            return worker_class.decrypt(key,input_text)