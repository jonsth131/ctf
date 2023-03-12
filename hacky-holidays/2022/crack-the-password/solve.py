#!/usr/bin/env python3

from z3 import *

def printModel(model):
    found = []

    for idx in range(0, length):
        strVal = str(model[flag[idx]])
        found.append(chr(int(strVal)))

    print(''.join(found))

length = 33

s = Solver()
flag = [BitVec(f"flag_{i}", 8) for i in range(0, length)]

s.add(flag[0] == 2 * flag[6] - 29)
s.add(flag[1] == flag[19] + 5)
s.add(flag[2] == (flag[8] >> 1) + 19)
s.add(flag[3] == flag[15] + 53)
s.add(flag[4] == flag[3] - 68)
s.add(flag[5] == flag[17] + 40)
s.add(flag[6] == flag[22] >> 1)
s.add(flag[7] == (flag[21] ^ flag[11]))
s.add(flag[8] == (flag[5] ^ 7))
s.add(flag[9] == flag[14] - 33)
s.add(flag[10] == flag[30] + 7)
s.add(flag[11] == 2 * flag[16])
s.add(flag[12] == flag[9] + flag[29])
s.add(flag[13] == 49)
s.add(flag[14] == 2 * flag[29] + 3)
s.add(flag[15] == (flag[0] ^ 5))
s.add(flag[16] == 2 * (flag[18] >> 1))
s.add(flag[17] == (flag[20] ^ 0x40))
s.add(flag[18] == (flag[23] ^ 0xA))
s.add(flag[19] == flag[7] - 2)
s.add(flag[20] == (flag[28] ^ flag[10]))
s.add(flag[21] == flag[25] >> 1)
s.add(flag[22] == (flag[31] | 0x61) - 2)
s.add(flag[23] == 57)
s.add(flag[24] == 2 * flag[18])
s.add(flag[25] == flag[26] + flag[16])
s.add(flag[26] == flag[11] / 2 + 7)
s.add(flag[27] == 2 * (flag[4] + 123))
s.add(flag[28] == flag[1] - 19)
s.add(flag[29] == flag[32] - 77)
s.add(flag[30] == flag[31] - flag[16])
s.add(flag[31] == 2 * flag[13] + 1)
s.add(flag[32] == flag[15] + flag[4])

if s.check() == unsat:
    print("No solution found")
    exit(1)

printModel(s.model())
