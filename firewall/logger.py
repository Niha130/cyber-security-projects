import datetime

def log_event(data):
    with open("logs/firewall.log", "a") as f:
        f.write(f"{datetime.datetime.now()} - {data}\n")
