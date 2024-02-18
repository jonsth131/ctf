from Crypto.Util.number import long_to_bytes

def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return (gcd, y - (b // a) * x, x)

def modinv(a, m):
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError('Modular inverse does not exist')
    else:
        return x % m

def decrypt(ct, p, q, r, e):
    n = p * q * r
    phi = (p - 1) * (q - 1) * (r - 1)
    d = modinv(e, phi)
    pt = pow(ct, d, n)
    return long_to_bytes(pt)

if __name__ == '__main__':
    p = 21942765653871439764422303472543530148312720769660663866142363370143863717044484440248869144329425486818687730842077
    q = p + 6
    r = p + 12
    e = 65537
    ct = 9953835612864168958493881125012168733523409382351354854632430461608351532481509658102591265243759698363517384998445400450605072899351246319609602750009384658165461577933077010367041079697256427873608015844538854795998933587082438951814536702595878846142644494615211280580559681850168231137824062612646010487818329823551577905707110039178482377985
    print(decrypt(ct, p, q, r, e).decode())