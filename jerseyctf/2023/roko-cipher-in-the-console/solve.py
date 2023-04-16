#!/usr/bin/env python3

encoded = 'f1stg}th10_ej{s__act_nam'

part1 = encoded[12:18]
part2 = encoded[18:24]
part3 = encoded[6:12]
part4 = encoded[0:6]

flag = ''

for i in range(len(part1)):
    flag += part1[i]
    flag += part2[i]
    flag += part3[i]
    flag += part4[i]

print(flag)
