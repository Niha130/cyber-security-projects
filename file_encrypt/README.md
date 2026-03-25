# Secure File Storage System (AES Encryption)

## Description
This project provides secure file encryption and decryption using AES (Fernet) with integrity verification using SHA-256.

## Features
- AES-based encryption (Fernet)
- File integrity verification (SHA-256)
- Secure key storage
- Logging system

## Tools Used
- Python
- cryptography
- hashlib

## How to Run
1. Create virtual environment:
   python3 -m venv venv
   source venv/bin/activate

2. Install dependencies:
   pip install -r requirements.txt

3. Run:
   python main.py

## Output
- Encrypted file with .enc extension
- Decrypted file restored
- Hash printed for integrity check
