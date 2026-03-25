# Personal Firewall using Python

## Description
This project is a lightweight personal firewall that monitors network traffic and blocks suspicious IP addresses.

## Features
- Real-time packet monitoring
- IP-based filtering
- Suspicious activity detection
- Logging system

## Tools Used
- Python
- Scapy
- Kali Linux

## How to Run
1. Create virtual environment:
   python3 -m venv venv
   source venv/bin/activate

2. Install dependencies:
   pip install scapy

3. Run:
   sudo venv/bin/python main.py

## Output
- Displays allowed and blocked packets
- Logs suspicious activity in logs/firewall.log
