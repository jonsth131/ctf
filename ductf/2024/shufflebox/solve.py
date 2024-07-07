#!/usr/bin/env python3

shuffle_pos = [9, 10, 0, 8, 11, 13, 3, 6, 15, 5, 14, 7, 4, 2, 12, 1]

def invert_perm(perm):
    inverse = [0] * len(perm)
    for i, p in enumerate(perm):
        inverse[p] = i
    return inverse

INV_PERM = invert_perm(shuffle_pos)

def reverse_perm(s):
    assert len(s) == 16
    return ''.join(s[INV_PERM[p]] for p in range(16))

decrypted = reverse_perm('owuwspdgrtejiiud')

print(f'DUCTF{{{decrypted}}}')
