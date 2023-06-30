```python
from cryptography.fernet import Fernet
from getpass import getpass

def generate_key():
    """
    Generate a new key for encryption and decryption
    """
    return Fernet.generate_key()

def encrypt(message: str, key: str) -> str:
    """
    Encrypt the message with the provided key
    """
    f = Fernet(key)
    return f.encrypt(message.encode()).decode()

def decrypt(token: str, key: str) -> str:
    """
    Decrypt the token with the provided key
    """
    f = Fernet(key)
    return f.decrypt(token.encode()).decode()

def encrypt_profile(profile):
    """
    Encrypt the profile with a password
    """
    password = getpass("Enter password for encryption: ")
    key = generate_key()
    encrypted_profile = encrypt(profile, key)
    return encrypted_profile, key

def decrypt_profile(encrypted_profile, key):
    """
    Decrypt the profile with the provided key
    """
    decrypted_profile = decrypt(encrypted_profile, key)
    return decrypted_profile
```