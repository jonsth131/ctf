#!/usr/bin/env python3

import sys
import requests


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f'Usage: {sys.argv[0]} <port>')
        sys.exit(1)

    URL = 'http://chal.ctf.games'
    PORT = sys.argv[1]

    print(f'[*] Connecting to {URL}:{PORT}')
    s = requests.Session()
    r = s.get(f'{URL}:{PORT}/site/flag.php', allow_redirects=False)

    flag = ''

    while r.status_code == 302:
        print(f'[*] Redirected to {r.headers["Location"]}')

        if r.text.startswith('character'):
            value = r.text.strip()[-1:]
            print(f'[*] Found character: {value}')
            flag += value

        r = s.get(
            f'{URL}:{PORT}{r.headers["Location"]}', allow_redirects=False)

    print(f'[+] Flag: {flag[:-1]}')
