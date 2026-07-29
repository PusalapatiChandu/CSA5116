# Monoalphabetic Cipher

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key = "QWERTYUIOPASDFGHJKLZXCVBNM"

encrypt_dict = {}
decrypt_dict = {}

for i in range(26):
    encrypt_dict[alphabet[i]] = key[i]
    decrypt_dict[key[i]] = alphabet[i]

plaintext = input("Enter Plaintext: ").upper()

ciphertext = ""

for ch in plaintext:
    if ch in encrypt_dict:
        ciphertext += encrypt_dict[ch]
    else:
        ciphertext += ch

print("Encrypted Text:", ciphertext)

decrypted = ""

for ch in ciphertext:
    if ch in decrypt_dict:
        decrypted += decrypt_dict[ch]
    else:
        decrypted += ch

print("Decrypted Text:", decrypted)
