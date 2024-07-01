# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 00:25:40 2024

@author: abdom
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 20:32:52 2024

@author: abdom
"""
import re

class CaesarCipher:
    global_key = {
        "a": "d", "b": "e", "c": "f", "d": "g", "e": "h", "f": "i", "g": "j",
        "h": "k", "i": "l", "j": "m", "k": "n", "l": "o", "m": "p", "n": "q", "o": "r", 
        "p": "s", "q": "t", "r": "u", "s": "v", "t": "w", "u": "x", "v": "y", "w": "z", 
        "x": "a", "y": "b", "z": "c", " ": " "
    }

    def __init__(self, encryption_key=None):
        if encryption_key is None:
            encryption_key = CaesarCipher.global_key
        self.encryption_key = encryption_key
        self.decryption_key = self.reverse_key(encryption_key)

    @staticmethod
    def reverse_key(key_taken):
        return {v: k for k, v in key_taken.items()}

    def encrypt_string(self, decr_mess:str()):
        enc_str = str()
        for char in decr_mess.lower():
            enc_str += self.encryption_key.get(char)
        return enc_str

    def decrypt_string(self, enc_mess):
        dec_str = []  # here we use the list and join method to get better performance  bc .join has better impelmentation in cython
        for char in enc_mess.lower():
            dec_str.append(self.decryption_key.get(char, char))
        return str().join(dec_str)

    
    def check_input(self,string):
        if re.match("^[A-Za-z\s]*$", string):
            print("Input is valid.")
        else:
            raise ValueError("Invalid input: Only alphabets and spaces are allowed.")

    def get_cipher(self, text : str() , key=None , encrypt=True ):
        if key is not None:
            self.encryption_key = key
            self.decryption_key = self.reverse_key(key)
        if encrypt:
            return self.encrypt_string(text)
        else:
            return self.decrypt_string(text)

'''
# Example usage
message = "Hello data engineers"
obj = CaesarCipher()

# Encrypt the message
encrypted_message = obj.encrypt_string(message)
print("Encrypted:", encrypted_message)

# Decrypt the message
decrypted_message = obj.decrypt_string(encrypted_message)
print("Decrypted:", decrypted_message)



# Encrypt the message
encrypted_message = obj.encrypt_string(message)
print("Encrypted:", encrypted_message)

# Decrypt the message
decrypted_message = obj.get_cipher(encrypted_message,encrypt=False)

'''