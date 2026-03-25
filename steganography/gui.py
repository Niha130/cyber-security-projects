import tkinter as tk
from steg import encode_image, decode_image

def encode():
    path = entry_image.get()
    text = entry_text.get()

    output = encode_image(path, text)
    result_label.config(text=f"Saved: {output}")

def decode():
    path = entry_image.get()
    message = decode_image(path)
    result_label.config(text=f"Message: {message}")

app = tk.Tk()
app.title("Steganography Tool")

tk.Label(app, text="Image Path").pack()
entry_image = tk.Entry(app, width=40)
entry_image.pack()

tk.Label(app, text="Secret Message").pack()
entry_text = tk.Entry(app, width=40)
entry_text.pack()

tk.Button(app, text="Encode", command=encode).pack()
tk.Button(app, text="Decode", command=decode).pack()

result_label = tk.Label(app, text="")
result_label.pack()

app.mainloop()
