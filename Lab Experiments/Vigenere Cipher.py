text = input("Enter Plaintext: ").upper()
key = input("Enter Key: ").upper()

# Repeat key
k = (key * (len(text)//len(key) + 1))[:len(text)]
print("Repeated Key:", k)

# Encryption
cipher = ""
for i in range(len(text)):
    cipher += chr((ord(text[i]) + ord(k[i]) - 130) % 26 + 65)

print("Cipher Text:", cipher)

# Decryption
plain = ""
for i in range(len(cipher)):
    plain += chr((ord(cipher[i]) - ord(k[i])) % 26 + 65)

print("Decrypted Text:", plain)
