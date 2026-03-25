from flask import Flask, request, render_template
from db import init_db, vulnerable_login
from detector import detect_sqli
from logger import log_attack
from utils import sanitize_input

app = Flask(__name__)
init_db()

@app.route('/', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if detect_sqli(username) or detect_sqli(password):
            log_attack(f"SQLi Attempt: {username} | {password}")
            return "SQL Injection Detected!"

        result = vulnerable_login(username, password)

        if result:
            return render_template("result.html", msg="Login Success")
        else:
            return render_template("result.html", msg="Login Failed")

    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
