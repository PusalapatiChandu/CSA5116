def key_matrix(key):
    key = key.upper().replace("J", "I")
    s = ""
    for c in key + "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if c.isalpha() and c not in s:
            s += c
    return [list(s[i:i+5]) for i in range(0, 25, 5)]

def pos(mat, ch):
    if ch == "J":
        ch = "I"
    for i in range(5):
        for j in range(5):
            if mat[i][j] == ch:
                return i, j

key = input("Enter Key: ")
text = input("Enter Plaintext: ").upper().replace("J", "I").replace(" ", "")

# Prepare text
prepared = ""
i = 0
while i < len(text):
    a = text[i]
    if i + 1 < len(text):
        b = text[i + 1]
        if a == b:
            prepared += a + "X"
            i += 1
        else:
            prepared += a + b
            i += 2
    else:
        prepared += a + "X"
        i += 1

mat = key_matrix(key)

print("\nKey Matrix:")
for row in mat:
    print(*row)

print("\nPrepared Text:", prepared)

cipher = ""
for i in range(0, len(prepared), 2):
    r1, c1 = pos(mat, prepared[i])
    r2, c2 = pos(mat, prepared[i + 1])

    if r1 == r2:
        cipher += mat[r1][(c1 + 1) % 5] + mat[r2][(c2 + 1) % 5]
    elif c1 == c2:
        cipher += mat[(r1 + 1) % 5][c1] + mat[(r2 + 1) % 5][c2]
    else:
        cipher += mat[r1][c2] + mat[r2][c1]

print("Cipher Text:", cipher)
