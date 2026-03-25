import datetime

def log(data):
    with open("logs/scan.log","a") as f:
        f.write(f"{datetime.datetime.now()} - {data}\n")
