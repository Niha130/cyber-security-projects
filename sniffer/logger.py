import datetime
from config import LOG_FILE

def log_alert(message):
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.datetime.now()} - {message}\n")
