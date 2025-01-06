#!/usr/bin/env python3
import binascii


def decode(input, key):
    decoded = ""
    for i in range(len(input)):
        decoded += chr(ord(input[i]) - ord(key[i]))

    return decoded


def get_key(input, keyed):
    key = ""
    for i in range(len(input)):
        key += chr(ord(keyed[i]) - ord(input[i]))

    return key


def uncatify(catified):
    charset = {
        '0': "🐱", '1': "🐈", '2': "😸", '3': "😹",
        '4': "😺", '5': "😻", '6': "😼", '7': "😽",
        '8': "😾", '9': "😿", 'A': "🙀", 'B': "🐱‍👤",
        'C': "🐱‍🏍", 'D': "🐱‍💻", 'E': "🐱‍👓", 'F': "🐱‍🚀",
    }

    charset = {v: k for k, v in charset.items()}

    uncatified = ""
    for i in range(len(catified)-1):
        if catified[i] in charset and catified[i+1] != "‍":
            uncatified += charset[catified[i]]
        elif catified[i-2] + catified[i-1] + catified[i] in charset:
            uncatified += charset[catified[i-2] + catified[i-1] + catified[i]]

    uncatified += charset[catified[-1]]
    return uncatified


def main():
    with open("example_input.txt", "r") as f:
        example_input = f.read().strip()

    print("Example input: {}".format(example_input))

    with open("example_output.txt", "r") as f:
        example_output = f.read().strip()

    print("Example output: {}".format(example_output))

    uncatified = uncatify(example_output)

    print("Uncatified: {}".format(uncatified))

    keyed = binascii.unhexlify(uncatified).decode("utf-8")

    print("Keyed: {}".format(keyed))

    print(
        f"Length of input: {len(example_input)}, length of keyed: {len(keyed)}")

    key = get_key(example_input, keyed)

    print("Key: {}".format(key))

    decoded = decode(keyed, key)

    print("Decoded: {}".format(decoded))

    with open("flag_output.txt", "r") as f:
        flag_output = f.read().strip()

    print("Flag output: {}".format(flag_output))

    uncatified = uncatify(flag_output)
    keyed = binascii.unhexlify(uncatified).decode("utf-8")
    decoded = decode(keyed, key)

    print("Flag: {}".format(decoded))


if __name__ == "__main__":
    main()
