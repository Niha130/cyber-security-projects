import datetime
from config import LOG_FILE
from crypto import encrypt_data

def log_key(key):
    timestamp = datetime.datetime.now()
    data = f"{timestamp} - {key}"
    encrypted = encrypt_data(data)

    with open(LOG_FILE, "ab") as f:
        f.write(encrypted + b"\n")
