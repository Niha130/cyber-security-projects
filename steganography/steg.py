from PIL import Image

def text_to_bin(text):
    return ''.join(format(ord(i), '08b') for i in text)

def bin_to_text(binary):
    chars = [binary[i:i+8] for i in range(0, len(binary), 8)]
    return ''.join(chr(int(c, 2)) for c in chars)

def encode_image(image_path, secret_text):
    img = Image.open(image_path)
    binary_text = text_to_bin(secret_text) + '1111111111111110'

    data = list(img.getdata())
    new_data = []

    data_index = 0

    for pixel in data:
        r, g, b = pixel

        if data_index < len(binary_text):
            r = (r & ~1) | int(binary_text[data_index])
            data_index += 1

        if data_index < len(binary_text):
            g = (g & ~1) | int(binary_text[data_index])
            data_index += 1

        if data_index < len(binary_text):
            b = (b & ~1) | int(binary_text[data_index])
            data_index += 1

        new_data.append((r, g, b))

    img.putdata(new_data)
    output_path = "output/encoded.png"
    img.save(output_path)

    return output_path

def decode_image(image_path):
    img = Image.open(image_path)
    binary_data = ""

    for pixel in list(img.getdata()):
        for color in pixel[:3]:
            binary_data += str(color & 1)

    end_marker = '1111111111111110'
    binary_data = binary_data.split(end_marker)[0]

    return bin_to_text(binary_data)
