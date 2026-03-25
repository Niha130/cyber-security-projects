import datetime
from config import LOG_FILE

def log_attack(data):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.datetime.now()} - {data}\n")
