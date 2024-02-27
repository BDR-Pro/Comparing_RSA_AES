from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
import time

start=time.time()
# Generate a private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=4089
)

# Get the public key from the private key
public_key = private_key.public_key()

# Serialize the private key to PEM format
private_key_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

# Serialize the public key to PEM format
public_key_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

end=time.time()
# Print the private and public keys
print("Private Key:")
print(private_key_pem.decode())

print("Public Key:")
print(public_key_pem.decode())

duration_ms = (end - start) * 1000
print("Time taken to generate the key pair: ", duration_ms, "ms")

start=time.time()

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import os

# Choose the key size for AES: 128, 192, or 256 bits (16, 24, or 32 bytes)
key_size_bytes = 32  # For AES-256
aes_key = os.urandom(key_size_bytes)  # Generate a random key

# Print the AES key
print("AES Key:")
print(aes_key.hex())

end=time.time()

duration_msAES = (end - start) * 1000
print("Time taken to generate the AES key: ", duration_msAES, "ms")


with open("result.txt", "w") as file:
    file.write("Private Key:\n")
    file.write(private_key_pem.decode())
    file.write("\nPublic Key:\n")
    file.write(public_key_pem.decode())
    file.write("\nAES Key:\n")
    file.write(aes_key.hex())
    file.write("\nTime taken to generate the key pair: ")
    file.write(str(duration_ms))
    file.write("ms\nTime taken to generate the AES key: ")
    file.write(str(duration_msAES))
    file.write("ms\n")
    
with open("private_key.pem", "wb") as key_file:
    key_file.write(private_key_pem)
