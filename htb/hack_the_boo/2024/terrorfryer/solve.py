#!/usr/bin/env python3

def main():
    scrambled_flag = list("1_n3}f3br9Ty{_6_rHnf01fg_14rlbtB60tuarun0c_tr1y3")
    test = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUV")
    scrambled_test = list("TzHLVAnNpJbkdlOsuaCSGwtyIUeojKgcQqmiMhBxRDfErFvP")

    mapping = []
    for i in range(len(test)):
        mapping.append(test.index(scrambled_test[i]))

    flag = [None] * len(scrambled_flag)
    i = 0
    for n in mapping:
        flag[n] = scrambled_flag[i]
        i += 1

    print("".join(flag))


if __name__ == "__main__":
    main()
