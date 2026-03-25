from flask import Flask, render_template, request
from api import check_ip
from db import init_db, save_result
from utils import format_result
from logger import log_event

app = Flask(__name__)
init_db()

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        ip = request.form['ip']

        data = check_ip(ip)
        result = format_result(data)

        save_result(ip, result)
        log_event(f"Checked IP: {ip} -> {result}")

        return render_template("result.html", result=result)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
