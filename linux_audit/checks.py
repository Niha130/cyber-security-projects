import os

def check_firewall():
    return os.system("ufw status") == 0

def check_ssh_root_login():
    try:
        with open("/etc/ssh/sshd_config") as f:
            for line in f:
                if "PermitRootLogin yes" in line:
                    return False
        return True
    except:
        return False

def check_shadow_permissions():
    return os.stat("/etc/shadow").st_mode & 0o777 == 0o640

def check_passwd_permissions():
    return os.stat("/etc/passwd").st_mode & 0o777 == 0o644
