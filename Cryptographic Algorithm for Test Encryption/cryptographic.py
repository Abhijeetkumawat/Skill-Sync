from cryptography.fernet import Fernet
import os

def generate_or_load_key():
    key_path = "encryption_key.key"
    if not os.path.exists(key_path):
        key = Fernet.generate_key()
        with open(key_path, "wb") as key_file:
            key_file.write(key)
    return open(key_path, "rb").read()

def encrypt_text(plain_text, key):
    cipher_suite = Fernet(key)
    cipher_text = cipher_suite.encrypt(plain_text.encode())
    return cipher_text

def decrypt_text(cipher_text, key):
    cipher_suite = Fernet(key)
    plain_text = cipher_suite.decrypt(cipher_text).decode()
    return plain_text

def main():
    key = generate_or_load_key()

    while True:
        print("\nChoose an option:")
        print("1. Encrypt Text")
        print("2. Decrypt Text")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            plain_text = input("Enter the text to encrypt: ")
            cipher_text = encrypt_text(plain_text, key)
            print("Encrypted Text:", cipher_text.hex())
        elif choice == '2':
            try:
                cipher_text_hex = input("Enter the hex-encoded encrypted text: ")
                cipher_text = bytes.fromhex(cipher_text_hex)
                decrypted_text = decrypt_text(cipher_text, key)
                print("Decrypted Text:", decrypted_text)
            except ValueError:
                print("Invalid hex input.")
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

main()
