import base64
from cryptography.fernet import Fernet


def encrypt_message(message, key):
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return base64.urlsafe_b64encode(encrypted_message).decode()


def decrypt_message(encrypted_message, key):
    f = Fernet(key)
    decrypted_message = f.decrypt(base64.urlsafe_b64decode(encrypted_message))
    return decrypted_message.decode()


if __name__ == '__main__':
    key = Fernet.generate_key()
    message = 'This is a secret message'
    encrypted_message = encrypt_message(message, key)
    decrypted_message = decrypt_message(encrypted_message, key)
    print('Original Message:', message)
    print('Encrypted Message:', encrypted_message)
    print('Decrypted Message:', decrypted_message)