#!/usr/bin/env python3
 
from z3 import *
 
def printModel(model):
    found = []
 
    for idx in range(0, length):
        strVal = str(model[flag[idx]])
        found.append(chr(int(strVal)))
 
    print(''.join(found))
 
length = 10
 
s = Solver()
flag = [BitVec(f"flag_{i}", 8) for i in range(0, length)]
 
s.add(flag[1] == 95)
s.add(9531 * flag[0] - 6756 * flag[1] + 8826 * flag[2] - 7295 * flag[3] - 4010 * flag[4] - 9218 * flag[5] + 1136 * flag[6] - 77 * flag[7] - 9947 * flag[8] + 1072 * flag[9] == -1722391)
s.add(2663 * flag[0] - 2620 * flag[1] + 1458 * flag[2] - 4929 * flag[3] - 1772 * flag[4] - 5452 * flag[5] + 5522 * flag[6] + 5795 * flag[7] - 5323 * flag[8] - 580 * flag[9] == -578655)
s.add(9576 * flag[0] - 7249 * flag[1] + 2094 * flag[2] - 3690 * flag[3] - 8522 * flag[4] + 8008 * flag[5] + 9082 * flag[6] + 8300 * flag[7] + 6611 * flag[8] + 3141 * flag[9] == 2808771)
s.add(7179 * flag[0] - 5969 * flag[1] - 4989 * flag[2] - 5826 * flag[3] - 4895 * flag[4] - 7765 * flag[5] - 9941 * flag[6] + 3040 * flag[7] - 2500 * flag[8] + 3765 * flag[9] == -2824381)
s.add(548 * flag[0] - 5100 * flag[1] - 2456 * flag[2] - 2977 * flag[3] - 6128 * flag[4] - 5099 * flag[5] + 888 * flag[6] - 2505 * flag[7] + 1132 * flag[8] - 4455 * flag[9] == -2775532)
s.add(1721 * flag[0] - 1391 * flag[1] - 7181 * flag[2] - 8001 * flag[3] + 3454 * flag[4] - 2644 * flag[5] + 845 * flag[6] + 7635 * flag[7] - 6953 * flag[8] + 2635 * flag[9] == -984357)
s.add(1399 * flag[0] - 9992 * flag[1] - 8259 * flag[2] - 8339 * flag[3] - 8954 * flag[4] - 8975 * flag[5] - 3898 * flag[6] - 340 * flag[7] - 5328 * flag[8] + 1224 * flag[9] == -5328888)
s.add(647 * flag[0] - 7816 * flag[1] + 7884 * flag[2] - 7008 * flag[3] - 8147 * flag[4] - 8519 * flag[5] + 994 * flag[6] + 5833 * flag[7] - 6726 * flag[8] + 9292 * flag[9] == -1430489)
s.add(7246 * flag[0] - 100 * flag[1] - 9831 * flag[2] - 1981 * flag[3] + 6913 * flag[4] + 716 * flag[5] + 748 * flag[6] - 58 * flag[7] + 8702 * flag[8] + 7763 * flag[9] == 2323434)
s.add(3113 * flag[0] - 3520 * flag[1] - 5650 * flag[2] + 153 * flag[3] - 9767 * flag[4] + 4689 * flag[5] - 7674 * flag[6] + 400 * flag[7] - 7529 * flag[8] + 5219 * flag[9] == -2081909)
 
if s.check() == unsat:
    print("No solution found")
    exit(1)
 
printModel(s.model())