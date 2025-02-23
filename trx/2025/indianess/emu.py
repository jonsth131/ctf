#!/usr/bin/env python3
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: emu.py <bytecode>")
        sys.exit(1)

    file = sys.argv[1]
    with open(file, "rb") as f:
        bytecode = f.read()

    registers = [0] * 8
    memory = [0] * (256 + 30)
    cmp = False
    flag = ""

    for i in range(0, len(bytecode), 4):
        opcode = bytecode[i:i+4]
        if len(opcode) < 4:
            break

        opcode = bytecode[i:i+2]
        p1 = bytecode[i+2]
        p2 = bytecode[i+3]

        # print(f"opcode: {opcode.hex()} p1: {p1} p2: {p2}")
        # print(f"registers: {registers}")

        match opcode:
            case b"\x00\x00":
                print(f"add: {registers[p1]} += {registers[p2]}")
                registers[p1] += registers[p2]
                registers[p1] &= 0xff
            case b"\x00\x05":
                print(f"add: {registers[p1]} += {p2}")
                registers[p1] += p2
                registers[p1] &= 0xff
            case b"\x00\x07":
                print(f"add: {registers[p1]} += {memory[registers[p2]]}")
                registers[p1] += memory[registers[p2]]
                registers[p1] &= 0xff
            case b"\x08\x0c":
                print(f"xor: {registers[p1]} ^= {memory[p2 + 256]}")
                registers[p1] ^= memory[p2 + 256]
            case b"\x09\x00":
                print(f"mov: {registers[p1]} = {registers[p2]}")
                registers[p1] = registers[p2]
            case b"\x09\x02":
                print(f"mov: {memory[p1]} = {memory[registers[p2]]}")
                memory[p1] = memory[registers[p2]]
            case b"\x09\x07":
                print(f"mov: {registers[p1]} = {memory[registers[p2]]}")
                registers[p1] = memory[registers[p2]]
            case b"\x09\x04":
                print(f"mov: {memory[registers[p1]]} = {memory[registers[p2]]}")
                memory[registers[p1]] = memory[registers[p2]]
            case b"\x09\x05":
                print(f"mov: {registers[p1]} = {p2}")
                registers[p1] = p2
            case b"\x09\x06":
                print(f"mov: {registers[p1]} = {memory[p2]}")
                registers[p1] = memory[p2]
            case b"\x09\x08":
                print(f"mov: {memory[p1]} = {p2}")
                memory[p1] = p2
            case b"\x09\x0b":
                print(f"mov: {memory[registers[p1]]} = {registers[p2]}")
                memory[registers[p1]] = registers[p2]
            case b"\x0a\x05":
                print(f"cmp: {registers[p1]} == {p2}")
                flag += chr(registers[p1] ^ p2)
                cmp = registers[p1] == p2
            case default:
                print(f"Invalid opcode {opcode.hex()}")

    print(f"flag: {flag}")
