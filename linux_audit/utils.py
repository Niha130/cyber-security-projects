from config import REPORT_FILE

def generate_report(results):
    with open(REPORT_FILE, "w") as f:
        for k, v in results.items():
            status = "PASS" if v else "FAIL"
            f.write(f"{k}: {status}\n")
