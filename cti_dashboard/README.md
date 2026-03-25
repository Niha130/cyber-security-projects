# Cyber Threat Intelligence Dashboard

## Description
This project provides real-time threat intelligence lookup using public APIs.

## Features
- IP reputation lookup
- Abuse score analysis
- Database storage
- Logging system

## Tools Used
- Python
- Flask
- Requests
- SQLite

## How to Run
1. Create virtual environment:
   python3 -m venv venv
   source venv/bin/activate

2. Install dependencies:
   pip install -r requirements.txt

3. Add API key in config.py

4. Run:
   python app.py

## Output
- Displays threat intelligence for IP
- Stores results in database
