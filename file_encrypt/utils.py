import hashlib
import datetime
from config import LOG_FILE

def generate_hash(filename):
    h = hashlib.sha256()

    with open(filename, "rb") as file:
        while chunk := file.read(4096):
            h.update(chunk)

    return h.hexdigest()

def log_event(data):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.datetime.now()} - {data}\n")
