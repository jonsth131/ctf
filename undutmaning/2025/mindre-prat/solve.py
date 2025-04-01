#!/usr/bin/env python3
from z3 import *


def printModel(model):
    found = []

    for idx in range(0, length):
        strVal = str(model[pw_vars[idx]])
        found.append(chr(int(strVal)))

    print(''.join(found))


length = 16

s = Solver()

pw_vars = [BitVec('pw_var_%d' % i, 8) for i in range(length)]

for i in range(length):
    s.add(pw_vars[i] >= ord('a'), pw_vars[i] <= ord('z'))

s.add(pw_vars[5] - pw_vars[3] < -4)
s.add(pw_vars[11] - pw_vars[0] == -5)
s.add(pw_vars[4] ^ pw_vars[12] == 2)
s.add(pw_vars[13] ^ pw_vars[1] == 19)
s.add(pw_vars[10] | pw_vars[1] == 126)
s.add(pw_vars[7] | pw_vars[4] == 108)
s.add(pw_vars[15] ^ pw_vars[6] == 16)
s.add(pw_vars[8] ^ pw_vars[9] == 9)
s.add(pw_vars[2] + pw_vars[11] == 226)
s.add(pw_vars[14] - pw_vars[3] == -5)
s.add(pw_vars[8] | pw_vars[7] == 125)
s.add(pw_vars[3] + pw_vars[11] < 226)
s.add(pw_vars[5] ^ pw_vars[9] == 8)
s.add(pw_vars[11] | pw_vars[10] == 111)
s.add(pw_vars[1] ^ pw_vars[3] == 2)
s.add(pw_vars[12] ^ pw_vars[2] == 25)
s.add(pw_vars[9] ^ pw_vars[15] == 26)

if s.check() == unsat:
    print("No solution found")
    exit(1)

printModel(s.model())
