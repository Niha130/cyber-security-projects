Vfrom config import BLOCKED_IPS

def is_blocked(ip):
    return ip in BLOCKED_IPS
