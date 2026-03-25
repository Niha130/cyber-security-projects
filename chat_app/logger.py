import datetime
from config import LOG_FILE

def log_message(data):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.datetime.now()} - {data}\n")
