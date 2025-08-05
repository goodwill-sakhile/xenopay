import base64
import hashlib
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from utils.logger import log_event

# AES configuration
BLOCK_SIZE = 16  # AES block size


def pad(data: bytes) -> bytes:
    """Applies PKCS7 padding."""
    padding_required = BLOCK_SIZE - len(data) % BLOCK_SIZE
    return data + bytes([padding_required] * padding_required)


def unpad(data: bytes) -> bytes:
    """Removes PKCS7 padding."""
    padding_length = data[-1]
    if padding_length > BLOCK_SIZE:
        raise ValueError("Invalid padding")
    return data[:-padding_length]


def derive_key(session_key: str) -> bytes:
    """
    Derives a 256-bit AES key from the session key using SHA-256.
    """
    key = hashlib.sha256(session_key.encode()).digest()
    return key


def encrypt_data(data: bytes, session_key: str) -> bytes:
    """
    Encrypts data using AES-256-CBC.
    """
    try:
        key = derive_key(session_key)
        iv = get_random_bytes(BLOCK_SIZE)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        padded_data = pad(data)
        encrypted = cipher.encrypt(padded_data)
        encrypted_payload = base64.b64encode(iv + encrypted)
        log_event("EncryptionEngine", f"Data encrypted: {len(encrypted_payload)} bytes.")
        return encrypted_payload
    except Exception as e:
        log_event("EncryptionEngine", f"Encryption failed: {e}")
        return b""


def decrypt_data(encrypted_payload: bytes, session_key: str) -> bytes:
    """
    Decrypts AES-256-CBC encrypted data.
    """
    try:
        raw = base64.b64decode(encrypted_payload)
        iv = raw[:BLOCK_SIZE]
        encrypted = raw[BLOCK_SIZE:]
        key = derive_key(session_key)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        decrypted = cipher.decrypt(encrypted)
        result = unpad(decrypted)
        log_event("EncryptionEngine", f"Data decrypted: {len(result)} bytes.")
        return result
    except Exception as e:
        log_event("EncryptionEngine", f"Decryption failed: {e}")
        return b""

