n = int(input("Enter matrix size: "))

print("Enter Key Matrix:")
key = [list(map(int, input().split())) for _ in range(n)]

text = input("Enter Plaintext: ").upper()

# Pad with X if needed
while len(text) % n != 0:
    text += "X"

print("Prepared Text:", text)

cipher = ""

for k in range(0, len(text), n):
    block = [ord(ch) - 65 for ch in text[k:k+n]]

    for i in range(n):
        s = 0
        for j in range(n):
            s += key[i][j] * block[j]
        cipher += chr((s % 26) + 65)

print("Cipher Text:", cipher)
