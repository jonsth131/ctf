import sys


def calculate_xmodem_crc(file_data):
    file_data = bytearray(file_data, 'utf-8')
    crc = 0

    def update_crc(crc, byte):
        crc ^= byte << 8
        for _ in range(8):
            if crc & 0x8000:
                crc = (crc << 1) ^ 0x1021
            else:
                crc <<= 1
        return crc & 0xFFFF

    for byte in file_data:
        crc = update_crc(crc, byte)

    return crc


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <command>")
        sys.exit(1)

    file_data = '#!/bin/bash\n'
    file_data += sys.argv[1]
    file_data += ' #'
    val = 0
    while True:
        crc = 0
        test_data = file_data + str(val)
        crc = calculate_xmodem_crc(test_data)
        if crc == 0xBBBB or crc == 0x3B75:
            print(f'Found CRC: {crc:04X}')
            print(f'file_data:\n{test_data}')
            sys.exit(0)

        val += 1
