#!/usr/bin/env python3

from z3 import *


def printModel(model):
    found = []

    for idx in range(0, length):
        strVal = str(model[flag_vars[idx]])
        found.append(chr(int(strVal)))

    print(''.join(found))


length = 22

s = Solver()
flag_vars = [BitVec(f'flag_{i}', 8) for i in range(0, length)]

s.add((flag_vars[18] * flag_vars[7] & flag_vars[12] ^ flag_vars[2]) == 36)
s.add((flag_vars[1] % flag_vars[14] - flag_vars[21] % flag_vars[15]) == -3)
s.add((flag_vars[10] + flag_vars[4] * flag_vars[11] - flag_vars[20]) == 5141)
s.add((flag_vars[19] + flag_vars[12] * flag_vars[0] ^ flag_vars[16]) == 8332)
s.add((flag_vars[9] ^ flag_vars[13] * flag_vars[8] & flag_vars[16]) == 113)
s.add((flag_vars[3] * flag_vars[17] + flag_vars[5] + flag_vars[6]) == 7090)
s.add((flag_vars[21] * flag_vars[2] ^ flag_vars[3] ^ flag_vars[19]) == 10521)
s.add((flag_vars[11] ^ flag_vars[20] * flag_vars[1] + flag_vars[6]) == 6787)
s.add((flag_vars[7] + flag_vars[5] - flag_vars[18] & flag_vars[9]) == 96)
s.add((flag_vars[12] * flag_vars[8] - flag_vars[10] + flag_vars[4]) == 8277)
s.add((flag_vars[16] ^ flag_vars[17] * flag_vars[13] + flag_vars[14]) == 4986)
s.add((flag_vars[0] * flag_vars[15] + flag_vars[3]) == 7008)
s.add((flag_vars[13] + flag_vars[18] * flag_vars[2] & flag_vars[5] ^ flag_vars[10]) == 118)
s.add((flag_vars[0] % flag_vars[12] - flag_vars[19] % flag_vars[7]) == 73)
s.add((flag_vars[14] + flag_vars[21] * flag_vars[16] - flag_vars[8]) == 11228)
s.add((flag_vars[3] + flag_vars[17] * flag_vars[9] ^ flag_vars[11]) == 11686)
s.add((flag_vars[15] ^ flag_vars[4] * flag_vars[20] & flag_vars[1]) == 95)
s.add((flag_vars[6] * flag_vars[12] + flag_vars[19] + flag_vars[2]) == 8490)
s.add((flag_vars[7] * flag_vars[5] ^ flag_vars[10] ^ flag_vars[0]) == 6869)
s.add((flag_vars[21] ^ flag_vars[13] * flag_vars[15] + flag_vars[11]) == 4936)
s.add((flag_vars[16] + flag_vars[20] - flag_vars[3] & flag_vars[9]) == 104)
s.add((flag_vars[18] * flag_vars[1] - flag_vars[4] + flag_vars[14]) == 5440)
s.add((flag_vars[8] ^ flag_vars[6] * flag_vars[17] + flag_vars[12]) == 7104)
s.add((flag_vars[11] * flag_vars[2] + flag_vars[15]) == 6143)

if s.check() == unsat:
    print("No solution found")
    exit(1)

printModel(s.model())
