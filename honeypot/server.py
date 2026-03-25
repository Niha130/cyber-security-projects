import socket
from config import HOST, PORT
from handler import handle_client

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)

    print(f"[+] Honeypot running on {HOST}:{PORT}")

    while True:
        conn, addr = server.accept()
        handle_client(conn, addr)
