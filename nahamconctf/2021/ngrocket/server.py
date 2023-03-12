#!/usr/bin/env python3

import socket
from Crypto.Cipher import AES

key = b''
iv = b''
ciphertext = b''
flag = bytearray('flag{................................}', 'utf-8')

def parse_data(data):
    global key
    global iv
    global ciphertext
    data = data.decode()
    split = data.split('\n')
    if len(data) > 4:
        key = bytearray.fromhex(split[3].replace(' ', '').replace('Key:', ''))
        iv = bytearray.fromhex(split[4].replace(' ', '').replace('IV:', ''))
    else:
        key = b''
        iv = b''
        ciphertext = b''
    
def handle_decrypted(decrypted):
    if b'flag' in decrypted:
        decrypted = decrypted.replace(b'\'', b'')
        split = decrypted.split(b' ')
        idx = int(split[7].decode())
        flag[idx] = ord(split[4].decode())
        check = flag.decode()
        if '.' in check:
            print(check)
        else:
            print('Flag found', check)
            exit(0)

def decrypt():
    global key
    global iv
    global ciphertext
    if key != b'' and iv != b'' and ciphertext != b'': 
        cipher = AES.new(key, AES.MODE_CBC, iv)
        encrypted = bytearray.fromhex(ciphertext.decode())
        decrypted = cipher.decrypt(encrypted)
        handle_decrypted(decrypted)
        key = b''
        iv = b''
        ciphertext = b''

HOST = '127.0.0.1'
PORT = 4444

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                if b'Key' in data:
                    parse_data(data)
                else:
                    ciphertext = data
                decrypt()
