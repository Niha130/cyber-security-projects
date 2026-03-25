import re

patterns = [
    r"(\bor\b|\band\b).*=.*",
    r"(--|#)",
    r"(union.*select)"
]

def detect_sqli(input_data):
    for pattern in patterns:
        if re.search(pattern, input_data.lower()):
            return True
    return False
