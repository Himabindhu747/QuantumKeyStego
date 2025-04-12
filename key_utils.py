
import os
import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def generate_random_key(length_bits=256):
    """Generates a random key of given bit length."""
    length_bytes = length_bits // 8
    return os.urandom(length_bytes)

def key_to_binary(key_bytes):
    """Converts key bytes to binary string."""
    return ''.join(f'{byte:08b}' for byte in key_bytes)

def binary_to_key(binary_str):
    """Converts binary string back to key bytes."""
    byte_chunks = [binary_str[i:i+8] for i in range(0, len(binary_str), 8)]
    return bytes(int(b, 2) for b in byte_chunks)

def hash_key_sha256(key_bytes):
    """Returns SHA-256 hash of the key."""
    return hashlib.sha256(key_bytes).digest()

def encrypt_key_aes(key_bytes, secret_pass):
    """Encrypts key using AES with a password."""
    secret = hashlib.sha256(secret_pass.encode()).digest()[:16]  # 128-bit key
    cipher = AES.new(secret, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(key_bytes, AES.block_size))
    return cipher.iv + ct_bytes  # Prepend IV for decryption

def decrypt_key_aes(encrypted_key, secret_pass):
    """Decrypts AES-encrypted key."""
    secret = hashlib.sha256(secret_pass.encode()).digest()[:16]
    iv = encrypted_key[:16]
    ct = encrypted_key[16:]
    cipher = AES.new(secret, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(ct), AES.block_size)
