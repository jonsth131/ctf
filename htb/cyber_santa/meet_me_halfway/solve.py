#!/usr/bin/env python3
import itertools
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

alphabet = '0123456789abcdef'
const = b'cyb3rXm45!@#'
generated_len = 16-len(const)

flag_ct = bytes.fromhex('31151620b1d564c47f597185f9a061a5601f0a316d649f9061c56fff52fa6101d9ffc663a796e550098c7b7a3652acae4b7c7a0b7fc24afb9df363335426d772e3a4e9e702584813c8fefbb3175f603ddb60db660ff25e92fe8618243b2e502e')
test_pt = bytes.fromhex('746573747465737474657374746573')
test_ct = bytes.fromhex('60dc6a74d7a091e0b2142c4bde041eed')

possibilities = [''.join(x) for x in itertools.product(alphabet, repeat=generated_len)]

k1s = [const + k.encode() for k in possibilities]
k2s = [k.encode() + const for k in possibilities]

print('[+] Generate first keys')
first_round = []
for k2 in k2s:
    cipher = AES.new(k2, mode=AES.MODE_ECB)
    first_round.append((k2, cipher.decrypt(test_ct)))

print('[+] Generate second keys')
second_round = []
for k1 in k1s:
    cipher = AES.new(k1, mode=AES.MODE_ECB)
    second_round.append(cipher.encrypt(pad(test_pt, 16)))

found_k1 = b''
found_k2 = b''

print('[+] Finding matches')
for (k2, first) in first_round:
    if first in second_round:
        k1 = b''
        for i in range(len(second_round)):
            if first == second_round[i]:
                k1 = k1s[i]
        print('[+] Found, k1:', k1, 'k2:', k2)
        found_k1 = k1
        found_k2 = k2
        break

cipher = AES.new(found_k2, mode=AES.MODE_ECB)
pt = cipher.decrypt(flag_ct)
cipher = AES.new(found_k1, mode=AES.MODE_ECB)
pt = cipher.decrypt(pt)
print(pt)
