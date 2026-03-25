from sniffer import start_sniffer
from utils import init_db

print("Starting Packet Sniffer... Press CTRL+C to stop")

init_db()
start_sniffer()
