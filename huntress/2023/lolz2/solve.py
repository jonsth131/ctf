#!/usr/bin/env python3

import base65536
import base64
import string


values = string.ascii_uppercase + string.ascii_lowercase
base = len(values)

encoded_flag = '籖ꍨ穉鵨杤𒅆象𓍆穉鵨詌ꍸ穌橊救硖穤歊晑硒敤睊ꉑ硊ꉤ晊ꉑ硆詤橆赑硤ꉑ穊赑硤詥楊ꉑ睖ꉥ橊赑睤ꉥ杊𐙑硬ꉒ橆𐙑硨穒祊ꉑ硖詤桊赑硤詥晊晑牙'

flag = base65536.decode(encoded_flag)
flag = base64.b64decode(flag)
flag = flag.decode('utf-8').split(',')[-1]

decoded_flag = ''
for i in range(0, len(flag), 2):
    first = values.index(flag[i])
    second = values.index(flag[i+1])
    decoded_flag += chr(first * base + second)

print(decoded_flag)
