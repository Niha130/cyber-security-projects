from logger import log_attack

def handle_client(conn, addr):
    ip = addr[0]
    print(f"[+] Connection from {ip}")
    log_attack(f"Connection from {ip}")

    conn.send(b"Fake SSH Service\nLogin: ")

    try:
        username = conn.recv(1024).decode().strip()
        conn.send(b"Password: ")
        password = conn.recv(1024).decode().strip()

        log_attack(f"{ip} -> {username}:{password}")

        conn.send(b"Access Denied\n")
    except:
        pass

    conn.close()
