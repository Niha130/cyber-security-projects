import matplotlib.pyplot as plt

def generate_report(alerts, counts):
    with open("reports/report.txt", "w") as f:
        f.write("ALERTS:\n")
        for alert in alerts:
            f.write(alert + "\n")

def plot_data(counts):
    ips = list(counts.keys())
    values = list(counts.values())

    plt.bar(ips, values)
    plt.xlabel("IP Address")
    plt.ylabel("Requests")
    plt.title("Traffic Analysis")
    plt.xticks(rotation=45)
    plt.show()
