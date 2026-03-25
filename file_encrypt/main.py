from encrypt import encrypt_file
from decrypt import decrypt_file
from utils import generate_hash, log_event

print("1. Encrypt File")
print("2. Decrypt File")

choice = input("Select option: ")

filename = input("Enter file name: ")

if choice == "1":
    enc_file = encrypt_file(filename)
    file_hash = generate_hash(enc_file)

    print("Encrypted file:", enc_file)
    print("Hash:", file_hash)

    log_event(f"Encrypted {filename} -> {enc_file} | Hash: {file_hash}")

elif choice == "2":
    dec_file = decrypt_file(filename)
    file_hash = generate_hash(dec_file)

    print("Decrypted file:", dec_file)
    print("Hash:", file_hash)

    log_event(f"Decrypted {filename} -> {dec_file} | Hash: {file_hash}")

else:
    print("Invalid option")
