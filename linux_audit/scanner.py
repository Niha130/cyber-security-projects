from checks import *
from logger import log_event

def run_scan():
    results = {}

    results["Firewall Enabled"] = check_firewall()
    results["SSH Root Login Disabled"] = check_ssh_root_login()
    results["/etc/shadow Secure"] = check_shadow_permissions()
    results["/etc/passwd Secure"] = check_passwd_permissions()

    for k, v in results.items():
        log_event(f"{k}: {v}")

    return results
