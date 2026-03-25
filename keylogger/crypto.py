from cryptography.fernet import Fernet
from config import KEY_FILE

def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as f:
        f.write(key)
    return key

def load_key():
    try:
        return open(KEY_FILE, "rb").read()
    except:
        return generate_key()

def encrypt_data(data):
    key = load_key()
    f = Fernet(key)
    return f.encrypt(data.encode())
