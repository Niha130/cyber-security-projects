def parse_logs(file):
    logs = []

    with open(file, "r") as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) > 3:
                logs.append({
                    "ip": parts[0],
                    "time": parts[1],
                    "request": parts[2]
                })

    return logs
