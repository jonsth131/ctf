#!/usr/bin/env python3
import random


def generate_flag(flag, seed):
    random.seed(seed)
    return ''.join(random.choices(flag, k=len(flag)*5))


def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]


def find_seed():
    flag = 'DUCTF{' + 'a' * 54 + '}'
    testval = 'aDaaaaaaaaaaaaaaCaaaaaaaFaaaFaTa}'
    for i in range(1337):
        out = generate_flag(flag, i)
        if out[:len(testval)] == testval:
            return i


def find_flag(seed):
    output = 'bDacadn3af1b79cfCma8bse3F7msFdT_}11m8cicf_fdnbssUc{UarF_d3m6T813Usca?tf_FfC3tebbrrffca}Cd18ir1ciDF96n9_7s7F1cb8a07btD7d6s07a3608besfb7tmCa6sasdnnT11ssbsc0id3dsasTs?1m_bef_enU_91_1ta_417r1n8f1e7479ce}9}n8cFtF4__3sef0amUa1cmiec{b8nn9n}dndsef0?1b88c1993014t10aTmrcDn_sesc{a7scdadCm09T_0t7md61bDn8asan1rnam}sU'
    flag = bytearray(61)
    for i in range(len(output)):
        test = generate_flag(flag.decode(), seed)
        if test == output:
            return flag.decode()
        for j in range(len(flag)):
            prev = flag[j]
            flag[j] = ord(output[i])
            t = generate_flag(flag.decode(), seed)
            if t[i] == output[i]:
                break
            flag[j] = prev

    print('Failed to find flag')


if __name__ == '__main__':
    seed = find_seed()
    print(f'Found seed: {seed}')
    flag = find_flag(seed)
    print(f'Flag: {flag}')
