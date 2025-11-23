from Cryptodome.Util.number import *
import random
import itertools

ciphertext = bytes.fromhex("2b542b2b182e122e1c2a04555107376d744376273b6d17741164197f457c191324456d5000200a757106640d1d73005576")  # actual ciphertext

un="111111111111111111111111111111111111111"

for nz in range(1, 8):
    print(nz)
    for indices in itertools.combinations(range(len(un)), nz):
        deux=list(un)
        for i in indices:
            deux[i] = "0"
        key = "".join(deux)
        random.seed(key)
        plaintext = b""
        for c in ciphertext:
           plaintext += bytes([c ^ random.randrange(0, 128)])
        
        if b"ZeroDays{" in plaintext:
            print(f"Key: {key}")
            print(f"Flag: {plaintext}")
            exit()


