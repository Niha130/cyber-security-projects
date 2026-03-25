from parser import parse_logs
from detector import detect_attacks
from utils import generate_report, plot_data
from config import LOG_FILE
from logger import log_event

print("Analyzing logs...\n")

logs = parse_logs(LOG_FILE)
alerts, counts = detect_attacks(logs)

for alert in alerts:
    print(alert)
    log_event(alert)

generate_report(alerts, counts)
plot_data(counts)

print("\nReport saved in reports/report.txt")
