from flask import Flask, render_template
from flask_socketio import SocketIO
from socket_handler import handle_message

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/chat')
def chat():
    return render_template("chat.html")

@socketio.on('send_message')
def message(data):
    handle_message(data)

if __name__ == "__main__":
    socketio.run(app, debug=True)
