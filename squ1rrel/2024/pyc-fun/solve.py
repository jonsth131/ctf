#!/usr/bin/env python3
import string

alphabet = string.ascii_letters + string.digits + "_{}"

key = [
    44,
    56,
    247,
    253,
    233,
    88,
    109,
    105,
    57,
    67,
    28,
    46,
    17,
    166,
    155,
    71,
    129,
    255,
    155,
    81,
    144,
    109,
    110,
    2,
    151,
    97,
    172,
    93,
    185,
    41,
    67,
    212,
]
result = [
    3807,
    2927,
    7947,
    5457,
    6217,
    1682,
    317,
    197,
    2647,
    2042,
    4052,
    3087,
    3127,
    8507,
    6742,
    1962,
    8907,
    8267,
    9312,
    557,
    9872,
    957,
    -3,
    3727,
    6502,
    3487,
    7947,
    2402,
    5657,
    3167,
    2202,
    6782,
]

flag = ""


def calc(c, k):
    val = ord(c) ^ k
    val = val << 3 | val >> 5
    val = val * 5 - 3
    return val


for i in range(len(result)):
    for c in alphabet:
        if calc(c, key[i]) == result[i]:
            flag += c
            break

print("Flag:", flag)
