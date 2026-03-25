# Network Packet Sniffer with Alert System

## Description
This project captures network traffic in real-time and detects suspicious activity based on packet frequency.

## Features
- Real-time packet capture
- IP-based traffic monitoring
- Anomaly detection (threshold-based)
- Logging system
- SQLite database storage

## Tools Used
- Python
- Scapy
- SQLite

## How to Run
1. Create virtual environment:
   python3 -m venv venv
   source venv/bin/activate

2. Install dependencies:
   pip install -r requirements.txt

3. Run:
   sudo venv/bin/python main.py

## Output
- Displays packet flow
- Alerts for suspicious IPs
- Logs stored in logs/alerts.log
