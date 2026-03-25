import datetime

def log_event(data):
    with open("logs/analysis.log", "a") as f:
        f.write(f"{datetime.datetime.now()} - {data}\n")
