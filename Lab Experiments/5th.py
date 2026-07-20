text = input("Enter Plaintext: ")

# Encryption
even = text[::2]
odd = text[1::2]
cipher = even + odd

print("Cipher Text:", cipher)

# Decryption
mid = (len(cipher) + 1) // 2
even = cipher[:mid]
odd = cipher[mid:]

plain = ""
for i in range(len(odd)):
    plain += even[i] + odd[i]
if len(even) > len(odd):
    plain += even[-1]

print("Decrypted Text:", plain)
