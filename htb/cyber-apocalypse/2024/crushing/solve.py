#!/usr/bin/env python3


def deserialize_and_recreate(file_data):
    char_map = [None] * 256
    for i in range(255):
        ptr_bytes = file_data.read(8)
        ptr = int.from_bytes(ptr_bytes, byteorder="little")

        indices = []
        for _ in range(ptr):
            index_bytes = file_data.read(8)
            index = int.from_bytes(index_bytes, byteorder="little")
            indices.append(index)

        char_map[i] = indices

    return char_map


if __name__ == "__main__":
    with open("message.txt.cz", "rb") as file:
        recreated_char_map = deserialize_and_recreate(file)

    message = [None] * 843

    for i in range(255):
        if recreated_char_map[i]:
            for item in recreated_char_map[i]:
                message[item] = chr(i)

    print("".join(message))
