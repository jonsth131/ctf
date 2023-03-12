#!/usr/bin/env python3

def decrypt_part(key, enc):
    enc = bytes.fromhex(enc)
    out = bytearray()
    for i in range(len(enc)):
        out.append(enc[i] ^ key[i])
    return out

parts = [
    (b'7bxvco1sj8gwpr92', '184D5825262C6336'),
    (b'0uctdhbg9rzyvq57', '6426435B4B626833'),
    (b'l3aupyodmehvzfk6', '045A125516100301'),
    (b'0upkfmbanov57z9x', '10161F05120C0B0F'),
    (b'6m2yx8fu9qd7kr4c', '454D53590B5D0507'),
    (b'2v6hqa0b9t3w5fjd', '5702161C19004442'),
    (b'n35aom7yfqzd04iu', '034646154F0F5259'),
    (b'93md6gizvlypw1ox', '52561D101614081C'),
    (b'txqgj3u5d9woz7na', '1156516D60641047'),
    (b'x5h3by9m0cre42k7', '1D150147420D564D'),
    (b'ehvuk4majq2tg10c', '03091A194B5D0315'),
    (b'8nmdwociyse0lab2', '574E190C124F141B'),
    (b'j9sfkvy3pwqxoeah', '0557144603171757'),
    (b'nw5s2kvijzqref9c', '1D575C071208191C'),
    (b'efbxmd4n5i8rkgya', '0902421A0844411D'),
    (b'1cnko9v30dp2rexf', '54074E0D004B565E'),
    (b'qp5oawce3uhvml21', '1803510A0413104B'),
    (b'lu94s012goyt8iba', '667F71510155115B'),
    (b'bsohq3igya5dr42n', '16530C071C561A49'),
    (b'gsz6oc7m9583krfi', '6D791C5A0E044C09'),
    (b'mb4xgiep72kcs1hv', '5D0C402754070412'),
    (b'l0rgne84jszcqxu6', '00552D0A0F064A04'),
    (b'xl5uba3zshrcdmjn', '0B113F7F2608575A'),
    (b'qofkayrevwml9gdx', '0800134B02180606'),
    (b'jcora4up78kbqs5t', '024306065E142118'),
    (b'43prh2zl0g9djqos', '5547500509415A05'),
    (b'8u2yiaj1pqwneb6s', '4C7F38320C041A11'),
    (b'759d2iwjhyqpl1vb', '5E411917570A050F'),
    (b'btvq9en5wgy1r4dx', '165A563A5C001E15'),
    (b'4yol2gx7mhijzur0', '5D0D4F1F53011D19'),
    (b'kz47slmu1cdrfhi6', '61701B18533F2836'),
    (b'qyw3zn9tmarix507', '233C23605A41167E')
]

decoded = ''
for part in parts:
    decoded += decrypt_part(part[0], part[1]).decode()

print(decoded)