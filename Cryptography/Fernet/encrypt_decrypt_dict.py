'''
Script to encrypt a dictionary in a file
and to decrypt into a dictionary, 
without saving a decrypted file
'''

import random, string
import pickle
from cryptography.fernet import Fernet

# Generate dictionary

def random_string(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

def generate_dict():
    dict = {}
    for i in range(10):
        dict[i] = {}
        dict[i]["name"] = random_string(10)
        dict[i]["value"] = random.uniform(-10, 10)
    return dict


# Write and read dict

def write_file(dict, filename):
    f = open(filename,"wb")
    pickle.dump(dict,f)
    f.close()
    return None


# Encryption and decryption

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
    '''
    pickle.load = Read a pickled object representation from the open file object file and return a dict.
    pickle.loads = Read a pickled object hierarchy from a bytes object and return a dict.
    '''
    dict = pickle.loads(decrypted_data)
    return dict




if __name__ == "__main__":
    dict = generate_dict()
    print(dict)
    write_file(dict, "dict.pkl")

    key = Fernet.generate_key()
    encrypt_file("dict.pkl", key)

    dict = decrypt_pkl("encrypted_dict.pkl", key)
    print(dict)
