#!/usr/bin/env python3

flag_ct = bytearray([11, 88, 18, 19, 72, 64, 105, 88, 83, 6, 8, 67, 108, 0, 20, 82, 11,
                    18, 104, 71, 17, 79, 107, 65, 16, 23, 1, 89, 85, 110, 81, 19, 1, 105, 22, 89, 85, 4])

key = b'm4st3r_l0cks_4r3nt_vry_str0ng_4r3_th3y'

flag = ''.join([chr(key[i] ^ flag_ct[i]) for i in range(len(key))])

print(flag)