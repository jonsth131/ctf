#!/usr/bin/env python3

val1 = 2 * 3 * 19 * 31 * 83 * 3331 * 165219437 * 550618493 * 66969810339969829
val2 = 1168302403781268101731523384107546514884411261

print(val1.to_bytes(19, 'big').decode() + val2.to_bytes(19, 'big').decode())
