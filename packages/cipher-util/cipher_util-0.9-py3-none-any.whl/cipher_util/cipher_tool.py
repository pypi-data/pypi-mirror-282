from cipher_util.caesar_cipher import CaesarCipher

def caesar_text_cipher(text, key=0, encrypt=True):
    caesar = CaesarCipher(key)
    if caesar.check_input(text):
        if encrypt:
            return caesar.encrypt_text(text)
        else:
            return caesar.decrypt_text(text)
