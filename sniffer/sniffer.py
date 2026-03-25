from scapy.all import sniff, IP
from analyzer import analyze_packet

def process_packet(pkt):
    if pkt.haslayer(IP):
        ip = pkt[IP].src
        print(f"Packet from {ip}")
        analyze_packet(ip)

def start_sniffer():
    sniff(prn=process_packet, store=0)
