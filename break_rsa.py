import sympy
import time
from Crypto.PublicKey import RSA
from Crypto.Util.number import inverse
from math import gcd


file_public_key = input("Enter the path of the public key file: ")

with open(file_public_key, "r") as f:
    key = RSA.importKey(f.read())

n = key.n
e = key.e

chrono = time.time()

factors = sympy.factorint(n)
print("Found factors in", time.time() - chrono, "seconds")

p, q = list(factors.keys())

print(f"p={p}, q={q}")

phi = (p - 1) * (q - 1)

d = inverse(e, phi)


private_key = RSA.construct((n, e, d, p, q))
private_key_pem = private_key.export_key()

private_key_file = "private_key.pem"
with open(private_key_file, "wb") as f:
    f.write(private_key_pem)

print(f"Private key generated and put in '{private_key_file}'")