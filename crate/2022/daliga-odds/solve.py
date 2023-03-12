from pwn import *
from mt19937predictor import MT19937Predictor

predictor = MT19937Predictor()
r = remote('challs.crate.nu', 16484)

r.recv()
r.recv()
r.recv()
r.recv()
r.recv()

r.recvuntil(b'guess? ')
for _ in range(624):
    r.sendline(b'1')
    data = r.recvuntil(b'guess? ')
    data = data.split(b'\n')[0].split(b' ')
    number = int(data[len(data)-1])
    print('Adding number:', number)
    predictor.setrandbits(number, 32)

r.sendline(str(predictor.getrandbits(32)).encode())
r.recvuntil(b'guess? ')
r.sendline(str(predictor.getrandbits(32)).encode())
print(r.recv())

r.close()