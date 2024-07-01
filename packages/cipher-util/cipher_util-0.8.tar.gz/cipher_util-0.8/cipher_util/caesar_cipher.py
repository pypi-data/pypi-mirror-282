import string
import re
alphas = {key:value for key , value in enumerate(string.ascii_uppercase)}

class CaesarCipher:
    def __init__(self , key):
        self.key = key

    def encrypt_text(self , text):
        ciphered = ''
        for letter in text:
            if re.match(r'\s+' , letter):
                ciphered += letter
            else:
                for key , value in alphas.items():
                    if letter.upper() == value:
                        shifts = (key + self.key) % 26 
                        ciphered += alphas[shifts] 
                        break
                    else:
                        pass
        return ciphered


    def decrypt_text(self , text):
        deciphered = ''
        for letter in text:
            if re.match(r'\s+' , letter):
                deciphered += letter
            else:
                for key , values in alphas.items():
                    if letter.upper() == values:
                        shifts = (key - self.key) % 26
                        deciphered += alphas[shifts]
                        break 
                    else: 
                        pass 
        return deciphered
    
    @staticmethod 
    def check_input(text):
        alphabets = string.ascii_uppercase
        alphabets += ' '
        for letter in text:
            if letter.upper() in alphabets:
                return True
            else:
                raise ValueError(f"{letter} not valid input, only alphabets and spaces allowed")
            
            