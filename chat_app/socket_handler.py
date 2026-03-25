from flask_socketio import emit
from crypto import encrypt_message, decrypt_message, generate_key
from logger import log_message

key = generate_key()

def handle_message(data):
    user = data['user']
    msg = data['message']

    encrypted = encrypt_message(key, msg)
    decrypted = decrypt_message(key, encrypted)

    log_message(f"{user}: {decrypted}")

    emit('response', {'user': user, 'message': decrypted}, broadcast=True)
