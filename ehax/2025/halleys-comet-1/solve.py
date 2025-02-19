#!/usr/bin/env python3

data = [
    72,
    75,
    54,
    91,
    128,
    51,
    99,
    106,
    50,
    122,
    114,
    104,
    99,
    113,
    126,
    99,
    105,
    125,
    99,
    50,
    114,
    99,
    119,
    50,
    113,
    105,
    99,
    50,
    121,
    108,
    105,
    118,
    99,
    103,
    50,
    113,
    105,
    121,
    99,
    34,
    105,
    121,
    55,
    99,
    107,
    50,
    99,
    121,
    108,
    105,
    118,
    105,
    130,
]

flag = ""

for i in data:
    if i > 120:
        flag += chr(i - 5)
    elif i > 98:
        flag += chr(i - 4)
    elif i > 70:
        flag += chr(i - 3)
    elif i >= 50:
        flag += chr(i - 2)
    else:
        flag += chr(i - 1)

print(flag)
