from config import THRESHOLD
from logger import log_alert
from utils import save_traffic

packet_count = {}

def analyze_packet(ip):
    packet_count[ip] = packet_count.get(ip, 0) + 1

    save_traffic(ip, packet_count[ip])

    if packet_count[ip] > THRESHOLD:
        msg = f"ALERT: Possible attack from {ip} (Packets: {packet_count[ip]})"
        print(msg)
        log_alert(msg)
