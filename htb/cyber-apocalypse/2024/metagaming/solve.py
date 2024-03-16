#!/usr/bin/env python3
import string
from itertools import product

alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits + "}_"


def gen_product(chars):
    yield from product(*([chars] * 4))


def run_regs0(flag):
    result = 0

    # Process first 4 characters of flag
    for i in range(4):
        result |= ord(flag[i]) << (i * 8)

    # Perform arithmetic operations
    result = (result + 2769503260) & 0xFFFFFFFF
    result = (result - 997841014) & 0xFFFFFFFF
    result ^= 4065997671
    result = (result + 690011675) & 0xFFFFFFFF
    result = (result + 540576667) & 0xFFFFFFFF
    result ^= 1618285201
    result = (result + 1123989331) & 0xFFFFFFFF
    result = (result + 1914950564) & 0xFFFFFFFF
    result = (result + 4213669998) & 0xFFFFFFFF
    result = (result + 1529621790) & 0xFFFFFFFF
    result = (result - 865446746) & 0xFFFFFFFF
    result = (result + 449019059) & 0xFFFFFFFF
    result = (result + 906976959) & 0xFFFFFFFF
    result = (result + 892028723) & 0xFFFFFFFF
    result = (result - 1040131328) & 0xFFFFFFFF
    result ^= 3854135066
    result ^= 4133925041
    result ^= 1738396966
    result = (result + 550277338) & 0xFFFFFFFF
    result = (result - 1043160697) & 0xFFFFFFFF

    return result


def run_regs1(flag):
    result = 0

    # Process next 4 characters of flag
    for i in range(4):
        result |= ord(flag[i + 4]) << (i * 8)

    # Perform arithmetic operations
    result ^= 1176768057
    result = (result - 2368952475) & 0xFFFFFFFF
    result ^= 2826144967
    result = (result + 1275301297) & 0xFFFFFFFF
    result = (result - 2955899422) & 0xFFFFFFFF
    result ^= 2241699318
    result = (result + 537794314) & 0xFFFFFFFF
    result = (result + 473021534) & 0xFFFFFFFF
    result = (result + 2381227371) & 0xFFFFFFFF
    result = (result - 3973380876) & 0xFFFFFFFF
    result = (result - 1728990628) & 0xFFFFFFFF
    result = (result + 2974252696) & 0xFFFFFFFF
    result = (result + 1912236055) & 0xFFFFFFFF
    result ^= 3620744853
    result ^= 2628426447
    result = (result - 486914414) & 0xFFFFFFFF
    result = (result - 1187047173) & 0xFFFFFFFF

    return result


def run_regs2(flag):
    result = 0

    # Process next 4 characters of flag
    for i in range(4):
        result |= ord(flag[i + 8]) << (i * 8)

    # Perform arithmetic operations
    result ^= 3103274804
    result = (result + 3320200805) & 0xFFFFFFFF
    result = (result + 3846589389) & 0xFFFFFFFF
    result ^= 2724573159
    result = (result - 1483327425) & 0xFFFFFFFF
    result ^= 1957985324
    result = (result - 1467602691) & 0xFFFFFFFF
    result = (result + 3142557962) & 0xFFFFFFFF
    result ^= 2525769395
    result = (result + 3681119483) & 0xFFFFFFFF
    result = (result - 1041439413) & 0xFFFFFFFF
    result = (result - 1042206298) & 0xFFFFFFFF
    result ^= 527001246
    result = (result - 855860613) & 0xFFFFFFFF
    result = (result + 1865979270) & 0xFFFFFFFF
    result = (result + 2752636085) & 0xFFFFFFFF
    result ^= 1389650363
    result = (result - 2721642985) & 0xFFFFFFFF
    result = (result + 3276518041) & 0xFFFFFFFF
    result ^= 1965130376

    return result


def run_regs3(flag):
    result = 0

    # Process next 4 characters of flag
    for i in range(4):
        result |= ord(flag[i + 12]) << (i * 8)

    # Perform arithmetic operations
    result ^= 3557111558
    result ^= 3031574352
    result = (result - 4226755821) & 0xFFFFFFFF
    result = (result + 2624879637) & 0xFFFFFFFF
    result = (result + 1381275708) & 0xFFFFFFFF
    result ^= 3310620882
    result ^= 2475591380
    result = (result + 405408383) & 0xFFFFFFFF
    result ^= 2291319543
    result = (result + 4144538489) & 0xFFFFFFFF
    result ^= 3878256896
    result = (result - 2243529248) & 0xFFFFFFFF
    result = (result - 561931268) & 0xFFFFFFFF
    result = (result - 3076955709) & 0xFFFFFFFF
    result = (result + 2019584073) & 0xFFFFFFFF
    result = (result + 1712479912) & 0xFFFFFFFF
    result ^= 2804447380
    result = (result - 2957126100) & 0xFFFFFFFF
    result = (result + 1368187437) & 0xFFFFFFFF
    result = (result + 3586129298) & 0xFFFFFFFF

    return result


def run_regs4(flag):
    result = 0

    # Process next 4 characters of flag
    for i in range(4):
        result |= ord(flag[i + 16]) << (i * 8)

    # Perform arithmetic operations
    result = (result - 1229526732) & 0xFFFFFFFF
    result = (result - 2759768797) & 0xFFFFFFFF
    result ^= 2112449396
    result = (result - 1212917601) & 0xFFFFFFFF
    result ^= 1524771736
    result = (result + 3146530277) & 0xFFFFFFFF
    result ^= 2997906889
    result = (result + 4135691751) & 0xFFFFFFFF
    result = (result + 1960868242) & 0xFFFFFFFF
    result = (result - 2775657353) & 0xFFFFFFFF
    result = (result + 1451259226) & 0xFFFFFFFF
    result = (result + 607382171) & 0xFFFFFFFF
    result = (result - 357643050) & 0xFFFFFFFF
    result ^= 2020402776

    return result


def run_regs5(flag):
    result = 0

    # Process next 4 characters of flag
    for i in range(4):
        result |= ord(flag[i + 20]) << (i * 8)

    # Perform arithmetic operations
    result = (result + 2408165152) & 0xFFFFFFFF
    result ^= 806913563
    result = (result - 772591592) & 0xFFFFFFFF
    result ^= 2211018781
    result = (result - 2523354879) & 0xFFFFFFFF
    result = (result + 2549720391) & 0xFFFFFFFF
    result ^= 3908178996
    result ^= 1299171929
    result = (result + 512513885) & 0xFFFFFFFF
    result = (result - 2617924552) & 0xFFFFFFFF
    result = (result + 390960442) & 0xFFFFFFFF
    result = (result + 1248271133) & 0xFFFFFFFF
    result = (result + 2114382155) & 0xFFFFFFFF
    result = (result - 2078863299) & 0xFFFFFFFF
    result = (result + 2857504053) & 0xFFFFFFFF
    result = (result - 4271947727) & 0xFFFFFFFF

    return result


def run_regs6(flag):
    result = 0

    # Process next 4 characters of flag
    for i in range(4):
        result |= ord(flag[i + 24]) << (i * 8)

    # Perform arithmetic operations
    result ^= 2238126367
    result ^= 1544827193
    result = (result + 4094800187) & 0xFFFFFFFF
    result ^= 3461906189
    result = (result - 1812592759) & 0xFFFFFFFF
    result ^= 1506702473
    result = (result + 536175198) & 0xFFFFFFFF
    result ^= 1303821297
    result = (result + 715409343) & 0xFFFFFFFF
    result ^= 4094566992
    result ^= 1890141105
    result ^= 3143319360

    return result


def run_regs7(flag):
    result = 0

    # Process next 4 characters of flag
    for i in range(4):
        result |= ord(flag[i + 28]) << (i * 8)

    # Perform arithmetic operations
    result = (result - 696930856) & 0xFFFFFFFF
    result ^= 926450200
    result = (result + 352056373) & 0xFFFFFFFF
    result = (result - 3857703071) & 0xFFFFFFFF
    result = (result + 3212660135) & 0xFFFFFFFF
    result = (result - 3854876250) & 0xFFFFFFFF
    result = (result + 3648688720) & 0xFFFFFFFF
    result ^= 2732629817
    result = (result - 2285138643) & 0xFFFFFFFF
    result ^= 2255852466
    result ^= 2537336944
    result ^= 4257606405

    return result


def run_regs8(flag):
    result = 0

    # Process next 4 characters of flag
    for i in range(4):
        result |= ord(flag[i + 32]) << (i * 8)

    # Perform arithmetic operations
    result = (result - 3703184638) & 0xFFFFFFFF
    result = (result - 2165056562) & 0xFFFFFFFF
    result = (result + 2217220568) & 0xFFFFFFFF
    result = (result + 2088084496) & 0xFFFFFFFF
    result = (result + 443074220) & 0xFFFFFFFF
    result = (result - 1298336973) & 0xFFFFFFFF
    result = (result + 822378456) & 0xFFFFFFFF
    result = (result + 2154711985) & 0xFFFFFFFF
    result = (result - 430757325) & 0xFFFFFFFF
    result ^= 2521672196

    return result


def run_regs9(flag):
    result = 0

    # Process next 4 characters of flag
    for i in range(4):
        result |= ord(flag[i + 36]) << (i * 8)

    # Perform arithmetic operations
    result = (result - 532704100) & 0xFFFFFFFF
    result = (result - 2519542932) & 0xFFFFFFFF
    result ^= 2451309277
    result ^= 3957445476
    result = (result + 2583554449) & 0xFFFFFFFF
    result = (result - 1149665327) & 0xFFFFFFFF
    result = (result + 3053959226) & 0xFFFFFFFF
    result = (result + 3693780276) & 0xFFFFFFFF
    result ^= 609918789
    result ^= 2778221635
    result = (result + 3133754553) & 0xFFFFFFFF
    result = (result + 3961507338) & 0xFFFFFFFF
    result ^= 1829237263
    result ^= 2472519933
    result = (result + 4061630846) & 0xFFFFFFFF
    result = (result - 1181684786) & 0xFFFFFFFF
    result = (result - 390349075) & 0xFFFFFFFF
    result = (result + 2883917626) & 0xFFFFFFFF
    result = (result - 3733394420) & 0xFFFFFFFF
    result ^= 3895283827
    result ^= 2257053750
    result = (result - 2770821931) & 0xFFFFFFFF
    result ^= 477834410

    return result


def brute(flag, func, checksum):
    for c in gen_product(alphabet):
        test = flag + "".join(c)
        result = func(test)
        if result == checksum:
            print("Found:", test)
            return test
    return None


def brute_force(checksums):
    flag = "HTB{"

    flag = brute(flag, run_regs1, checksums[1])
    flag = brute(flag, run_regs2, checksums[2])
    flag = brute(flag, run_regs3, checksums[3])
    flag = brute(flag, run_regs4, checksums[4])
    flag = brute(flag, run_regs5, checksums[5])
    flag = brute(flag, run_regs6, checksums[6])
    flag = brute(flag, run_regs7, checksums[7])
    flag = brute(flag, run_regs8, checksums[8])
    flag = brute(flag, run_regs9, checksums[9])

    return flag


def get_checksums():
    target = [
        0x3EE88722,
        0xECBDBE2,
        0x60B843C4,
        0x5DA67C7,
        0x171EF1E9,
        0x52D5B3F7,
        0x3AE718C0,
        0x8B4AACC2,
        0xE5CF78DD,
        0x4A848EDF,
    ]
    res = [0x8F]
    for i in range(len(target) - 1, -1, -1):
        res.append(target[i] ^ res[-1])

    return res[::-1]


if __name__ == "__main__":
    checksums = get_checksums()

    flag = brute_force(checksums)
    # flag = "HTB{m4n_1_l0v4_cXX_TeMpl4t35_9fb60c17b0}"

    result = run_regs0(flag)
    assert result == checksums[0]
    result = run_regs1(flag)
    assert result == checksums[1]
    result = run_regs2(flag)
    assert result == checksums[2]
    result = run_regs3(flag)
    assert result == checksums[3]
    result = run_regs4(flag)
    assert result == checksums[4]
    result = run_regs5(flag)
    assert result == checksums[5]
    result = run_regs6(flag)
    assert result == checksums[6]
    result = run_regs7(flag)
    assert result == checksums[7]
    result = run_regs8(flag)
    assert result == checksums[8]
    result = run_regs9(flag)
    assert result == checksums[9]

    print("Flag:", flag)
