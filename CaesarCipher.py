class CaesarCipher:
    def __init__(self, text: str, rotate = 3) -> str:
        self.text = text
        self.rotate = rotate

    def encrypt(self):
        encrypted_text = ""
        for x in self.text:
            if str(x) == "\n":
                encrypted_text += "\n"
            else:
                encode = ord(x) + self.rotate
                encrypted_text += chr(encode)
        return encrypted_text
    
    def decrypt(self):
        decrypted_text = ""
        for x in self.text:
            if str(x) == "\n":
                decrypted_text += "\n"
            else:
                encode = ord(x) - self.rotate
                decrypted_text += chr(encode)
        return decrypted_text

def file():
    return __file__

if __name__ == "__main__":
    pass