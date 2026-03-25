import requests
from config import PAYLOADS, TIMEOUT
from utils import log

def scan(url):
    results = []

    for payload in PAYLOADS:
        try:
            r = requests.get(url + "?q=" + payload, timeout=TIMEOUT)

            if payload in r.text:
                results.append(("XSS", payload))

            if "sql" in r.text.lower():
                results.append(("SQLi", payload))

        except Exception as e:
            log(f"Error: {e}")

    log(f"{url} -> {results}")
    return results
