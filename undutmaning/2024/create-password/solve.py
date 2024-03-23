#!/usr/bin/env python3

from pwn import *
import re

r = remote("0.cloud.chals.io", 16992)

data = r.recvuntil(b"password: ")
data = data.decode()
traveller_number = int(re.findall(r"#(\d+)!", data)[0])
print("Traveller number:", traveller_number)
print("Traveller number in hex:", hex(traveller_number))

divisor = 0

if traveller_number % 2 == 0:
    divisor = 2
else:
    print("Traveller number is not divisible by 2")
    exit()

traveller_number = traveller_number // divisor

password = f"KOKO{hex(traveller_number)}sn0o{divisor}ootEN0000000".encode()

print("Password:", password)
r.sendline(password)

tn = re.findall(r"\d", hex(traveller_number))
tn = [int(i) for i in tn]
digit_sum = sum(tn) + divisor

data = r.recvuntil(b"password: ")
data = data.decode()
digit_sum = int(re.findall(r"\d+", data)[-1]) - digit_sum

nines = digit_sum // 9
remainder = digit_sum % 9

password = password + str(remainder).encode() + b"9" * nines

print("New password:", password)

r.sendline(password)

data = r.recvall()

flag = re.findall(r"undut{.*}", data.decode())[0]
print("Flag:", flag)
