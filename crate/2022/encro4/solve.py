#!/usr/bin/env python3
import base64

msg= 'ZDE1N2Y2ZDMwMmRlMTBkOGUxNjM0ZmVhOWRiYWZlMDg5MTNkZWE2NzQxNTExZDEwNzI1Y2UxZmNkMTE5ZGJiNDA0MDgwNmM0MGU3YWJhMGMzMGQ2M2NmYjU3MDllMGVkOWZlOAo='

known_pt = b'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
known_ct = bytes.fromhex('d344f6c606dc05dffb714fe691bac007893fe0634c6f09057253dff3df16d9b03a0206cb306dba1f30e83bfb4404e8eb8af4')

ks = bytearray()

for i in range(len(known_pt)):
    ks.append(known_pt[i] ^ known_ct[i])

ct = bytes.fromhex(base64.b64decode(msg).decode())

pt = bytearray()
for i in range(len(ct)):
    pt.append(ks[i] ^ ct[i])

print(pt.decode())