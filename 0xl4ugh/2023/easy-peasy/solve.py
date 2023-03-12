#!/usr/bin/env python3

import string

"""
  local_58 = 0x7414c464;
  local_54 = 0x50534b7;
  local_50 = 0xf53513f5;
  local_4c = 0xc6030334;
  local_48 = 0x534323f5;
  local_44 = 0x53437323;
  local_40 = 0xd763;
"""
flag = bytes.fromhex('64c41474b7340505f51335f5340303c6f52343532373435363d7')
found = ''

print('Flag length:', len(flag))


def calc_char(chr):
    return ((ord(chr) & 0xf) << 4 | ord(chr) >> 4)


for i in range(len(flag)):
    for c in string.printable:
        val = calc_char(c)
        if flag[i] == val:
            found += c
            break

print('Found length:', len(found))
print(found)
