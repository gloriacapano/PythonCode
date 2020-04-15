from cryptography.fernet import Fernet

def generate_key():
    return Fernet.generate_key()


def encrypt_token(token, key):
    f= Fernet(key)
    return f.encrypt(token)


def decrypt_token(encrypted_token, key):
    f = Fernet(key)
    return f.decrypt(token)


#########################################################


def encrypt_file(filename, key):
    f = Fernet(key)
    with open(filename, 'rb') as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open("encrypted_"+filename, "wb") as file:
        file.write(encrypted_data)


def decrypt_file(filename, key):
    f = Fernet(key)
    with open(filename, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open("decrypted_" + filename, "wb") as file:
        file.write(decrypted_data)


if __name__ == "__main__":
    filename="TheRaven.txt"
    key = generate_key()
    encrypt_file(filename, key)
    decrypt_file("encrypted_"+filename, key)