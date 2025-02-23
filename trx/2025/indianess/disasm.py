#!/usr/bin/env python3
import sys


def disassemble(bytecode):
    disassembled = []
    for i in range(0, len(bytecode), 4):
        curr = dissasemble_opcode(bytecode[i:i+4])
        disassembled.append(curr)
    return disassembled


def dissasemble_opcode(opcode):
    if len(opcode) != 4:
        if opcode == b"\x0b":
            return "eq"
        return f"Invalid opcode {opcode.hex()}"
    opcode, p1, p2 = opcode[0:2], opcode[2], opcode[3]
    match opcode:
        case b"\x00\x00":
            """
            case 0:
              s[*(unsigned __int8 *)(i + 2LL + opcodes) - 8] += s[*(unsigned __int8 *)(i + 3LL + opcodes) - 8];
              i += 4;
              break;
            """
            return f"{opcode.hex()}: registry[{p1}] += registry[{p2}]"
        case b"\x00\x05":
            """
            case 5:
              s[*(unsigned __int8 *)(i + 2LL + opcodes) - 8] += *(_BYTE *)(i + 3LL + opcodes);
              i += 4;
              break;
            """
            return f"{opcode.hex()}: registry[{p1}] += {p2}"
        case b"\x00\x07":
            """
        case 7:
              s[*(unsigned __int8 *)(i + 2LL + opcodes) - 8] += s[(unsigned __int8)s[*(unsigned __int8 *)(i + 3LL + opcodes)
                                                                                   - 8]];
              i += 4;
              break;
            """
            return f"{opcode.hex()}: registry[{p1}] += mem[registry[{p2}]]"
        case b"\x08\x0c":
            """
        case 0xC:
              s[*(unsigned __int8 *)(i + 2LL + opcodes) - 8] ^= s[*(unsigned __int8 *)(i + 3LL + opcodes) + 256];
              i += 4;
              break;
            """
            return f"{opcode.hex()}: registry[{p1}] ^= mem[{p2} + 256]"
        case b"\x09\x00":
            """
            case 0:
              s[*(unsigned __int8 *)(i + 2LL + opcodes) - 8] = s[*(unsigned __int8 *)(i + 3LL + opcodes) - 8];
              i += 4;
              break;
            """
            return f"{opcode.hex()}: registry[{p1}] = registry[{p2}]"
        case b"\x09\x02":
            """
            case 2:
              s[*(unsigned __int8 *)(i + 2LL + opcodes)] = s[(unsigned __int8)s[*(unsigned __int8 *)(i + 3LL + opcodes)
                                                                              - 8]];
              i += 4;
              break;
            """
            return f"{opcode.hex()}: mem[{p1}] = mem[registry[{p2}]]"
        case b"\x09\x07":
            """
        case 7:
              s[*(unsigned __int8 *)(i + 2LL + opcodes) - 8] = s[(unsigned __int8)s[*(unsigned __int8 *)(i + 3LL + opcodes)
                                                                                  - 8]];
              i += 4;
              break;
            """
            return f"{opcode.hex()}: registry[{p1}] = mem[registry[{p2}]]"
        case b"\x09\x04":
            """
            case 4:
              s[(unsigned __int8)s[*(unsigned __int8 *)(i + 2LL + opcodes) - 8]] = s[(unsigned __int8)s[*(unsigned __int8 *)(i + 3LL + opcodes) - 8]];
              i += 4;
              break;
            """
            return f"{opcode.hex()}: mem[registry[{p1}]] = mem[registry[{p2}]]"
        case b"\x09\x05":
            """
            case 5:
              s[*(unsigned __int8 *)(i + 2LL + opcodes) - 8] = *(_BYTE *)(opcodes + i + 3LL);
              i += 4;
              break;
            """
            return f"{opcode.hex()}: registry[{p1}] = {p2}"
        case b"\x09\x06":
            """
            case 6:
              s[*(unsigned __int8 *)(i + 2LL + opcodes) - 8] = s[*(unsigned __int8 *)(i + 3LL + opcodes)];
              i += 4;
              break;
            """
            return f"{opcode.hex()}: registry[{p1}] = mem[{p2}]"
        case b"\x09\x08":
            """
            case 8:
              s[*(unsigned __int8 *)(i + 2LL + opcodes)] = *(_BYTE *)(opcodes + i + 3LL);
              i += 4;
              break;
            """
            return f"{opcode.hex()}: mem[{p1}] = {p2}"
        case b"\x09\x0b":
            """
            case 0xB:
              s[(unsigned __int8)s[*(unsigned __int8 *)(i + 2LL + opcodes) - 8]] = s[*(unsigned __int8 *)(i + 3LL + opcodes)
                                                                                   - 8];
              i += 4;
              break;
            """
            return f"{opcode.hex()}: mem[registry[{p1}]] = registry[{p2}]"
        case b"\x0a\x05":
            """
         case 5:
              v22 = (s[*(unsigned __int8 *)(i + 2LL + opcodes) - 8] == *(_BYTE *)(i + 3LL + opcodes)) & (unsigned __int8)v22;
              i += 4;
              break;
          """
            return f"{opcode.hex()}: registry[{p1}] == {p2}"
    return f"Invalid opcode {opcode.hex()}"


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: disasm.py <bytecode>")
        sys.exit(1)

    file = sys.argv[1]
    with open(file, "rb") as f:
        bytecode = f.read()

    instructions = disassemble(bytecode)
    for instr in instructions:
        print(instr)
