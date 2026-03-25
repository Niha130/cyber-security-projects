from scanner import run_scan
from utils import generate_report

print("Running Linux Security Audit...\n")

results = run_scan()

for k, v in results.items():
    print(f"{k}: {'PASS' if v else 'FAIL'}")

generate_report(results)

print("\nReport saved in reports/audit_report.txt")
