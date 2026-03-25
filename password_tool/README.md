# Password Strength Analyzer & Wordlist Generator

## Description
This tool evaluates password strength and generates custom wordlists based on personal inputs.

## Features
- Password strength analysis using zxcvbn
- Feedback on password weaknesses
- Custom wordlist generation
- Logging system

## Tools Used
- Python
- zxcvbn

## How to Run
1. Create virtual environment:
   python3 -m venv venv
   source venv/bin/activate

2. Install dependencies:
   pip install -r requirements.txt

3. Run:
   python main.py

## Output
- Strength score displayed
- Wordlist saved in wordlists/custom.txt
