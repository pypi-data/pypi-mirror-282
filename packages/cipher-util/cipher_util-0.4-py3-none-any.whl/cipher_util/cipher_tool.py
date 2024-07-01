from caesar_cipher import CaesarCipher

def caesar_text_cipher(text , key=0, encrypt=True):
    caeasr = CaesarCipher(key)
    if caeasr.check_input(text):
        if encrypt == True:
            return caeasr.encrypt_text(text)
        else:
            return caeasr.decrypt_text(text)
 




