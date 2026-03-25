def detect_attacks(logs):
    ip_count = {}
    alerts = []

    for log in logs:
        ip = log["ip"]
        ip_count[ip] = ip_count.get(ip, 0) + 1

        if ip_count[ip] > 5:
            alerts.append(f"Brute-force suspected from {ip}")

    return alerts, ip_count
