# Honeypot Server for Attack Detection

## Description
This project simulates a fake SSH service to capture attacker behavior.

## Features
- Fake login prompt
- Credential capture
- IP logging
- Attack monitoring

## Tools Used
- Python
- Socket programming

## How to Run
1. Create virtual environment:
   python3 -m venv venv
   source venv/bin/activate

2. Run:
   python main.py

3. Test:
   nc 127.0.0.1 2222

## Output
- Logs attacker IP and credentials
- Stored in logs/attacks.log
