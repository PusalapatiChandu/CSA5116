# Caesar Cipher
plain_text = input("Enter the plain text: ")
key = int(input("Enter the key value: "))
cipher_text = ""
for ch in plain_text:
    if ch.isupper():
        cipher_text += chr((ord(ch)-65+key)%26+65)
    elif ch.islower():
        cipher_text += chr((ord(ch)-97+key)%26+97)
    else:
        cipher_text += ch
print("Encrypted Text:", cipher_text)
decrypted_text=""
for ch in cipher_text:
    if ch.isupper():
        decrypted_text += chr((ord(ch)-65-key)%26+65)
    elif ch.islower():
        decrypted_text += chr((ord(ch)-97-key)%26+97)
    else:
        decrypted_text += ch
print("Decrypted Text:", decrypted_text)

