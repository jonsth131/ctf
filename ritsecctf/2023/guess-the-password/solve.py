import hashlib


key = '657fa7558ae9011e8b9d3f56d5c083273557c3139f27d7b62cac458eb1a1a19d'


def hash(user_input):
    salt = "RITSEC_Salt"
    return hashlib.sha256(salt.encode() + user_input.encode()).hexdigest()


for i in range(100000000):
    val = str(i).zfill(8)
    h = hash(val)
    if h == key:
        print('Found key:', val)
        exit(0)
