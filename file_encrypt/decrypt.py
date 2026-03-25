from cryptography.fernet import Fernet
from config import KEY_FILE

def decrypt_file(filename):
    key = open(KEY_FILE, "rb").read()
    f = Fernet(key)

    with open(filename, "rb") as file:
        encrypted = file.read()

    decrypted = f.decrypt(encrypted)

    output = filename.replace(".enc", "_decrypted")

    with open(output, "wb") as file:
        file.write(decrypted)

    return output
