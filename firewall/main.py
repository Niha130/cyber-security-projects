from scapy.all import sniff, IP
from rules import is_blocked
from logger import log_event
from utils import format_packet

packet_count = {}

def process_packet(pkt):
    if pkt.haslayer(IP):
        ip = pkt[IP].src

        packet_count[ip] = packet_count.get(ip, 0) + 1

        if is_blocked(ip):
            print(f"[BLOCKED] {ip}")
            log_event(f"Blocked IP: {ip}")
        else:
            print(f"[ALLOWED] {format_packet(ip)}")

        # Alert for suspicious activity
        if packet_count[ip] > 5:
            alert_msg = f"Suspicious activity detected from {ip}"
            print("[ALERT]", alert_msg)
            log_event(alert_msg)

print("Starting Personal Firewall... Press CTRL+C to stop.")
sniff(prn=process_packet, store=0)
