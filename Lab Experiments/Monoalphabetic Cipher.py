from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
key=input("Enter 8-character key: ").encode()
plaintext=input("Enter the plain text: ")
cipher=DES.new(key, DES.MODE_ECB)
encrypted=cipher.encrypt(pad(plaintext.encode(), DES.block_size))
print(encrypted.hex())
print(unpad(cipher.decrypt(encrypted),DES.block_size).decode())

