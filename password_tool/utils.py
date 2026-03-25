def save_wordlist(words):
    with open("wordlists/custom.txt", "w") as f:
        for w in words:
            f.write(w + "\n")

def log_result(data):
    with open("logs/results.log", "a") as f:
        f.write(data + "\n")
