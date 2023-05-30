ciphertext = "VHFUHW"

for i in range(25):
    plaintext = ""
    for c in ciphertext:
        if c.isalpha():
            plaintext += chr((ord(c) - ord('A') + 1) % 26 + ord('A'))
        else:
            plaintext += c
    print("k = %d: %s" % (i + 1, plaintext))
    ciphertext = plaintext