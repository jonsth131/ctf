#!/usr/bin/env python3
import struct

HEADER = b'\x50\x4b\x03\x04\x79\x85'

OP_CODES = {
    0x00: 'MOV',
    0x01: 'ADD',
    0x02: 'SUB',
    0x03: 'XOR',
    0x04: 'AND',
    0x05: 'OR',
    0x06: 'STACK',
    0x07: 'WRITE',
    0x08: 'READ',
    0x09: 'CMP',
    0x0a: 'CND_JMP',
    0x0b: 'SYSCALL'
}


REGISTERS = {
    0x00: 'R0',
    0x01: 'R1',
    0x02: 'R2',
    0x03: 'R3',
    0x04: 'R4',
    0x05: 'R5',
    0x06: 'R6'
}


def handle_conditional_jump(jmp_amount, pc):
    jmp_amount = int.from_bytes(jmp_amount, byteorder='little', signed=True)
    return 'CND_JMP ' + "0x{:04x}".format(pc + jmp_amount + 1)


def handle_syscall(arg1):
    if arg1 == 1:
        return 'SYSCALL: READ'
    elif arg1 == 2:
        return 'SYSCALL: WRITE'
    elif arg1 == 3:
        return 'SYSCALL: EXIT'
    else:
        return 'SYSCALL: UNKNOWN'


def handle_mov(arg1, arg2):
    if arg1 in REGISTERS:
        return 'MOV ' + REGISTERS[arg1] + ' 0x{:02x}'.format(arg2)
    else:
        return 'MOV 0x{:02x} 0x{:02x}'.format(arg1, arg2)


def handle_xor(arg1, arg2):
    if arg1 in REGISTERS and arg2 in REGISTERS:
        return 'XOR ' + REGISTERS[arg1] + ' ' + REGISTERS[arg2]
    else:
        return 'XOR 0x{:02x} 0x{:02x}'.format(arg1, arg2)


def handle_cmp(arg1, arg2):
    if arg1 in REGISTERS and arg2 in REGISTERS:
        return 'CMP ' + REGISTERS[arg1] + ' ' + REGISTERS[arg2]
    else:
        return 'CMP 0x{:02x} 0x{:02x}'.format(arg1, arg2)


def handle_add(arg1, arg2):
    if arg1 in REGISTERS and arg2 in REGISTERS:
        return 'ADD ' + REGISTERS[arg1] + ' ' + REGISTERS[arg2]
    else:
        return 'ADD 0x{:02x} 0x{:02x}'.format(arg1, arg2)


def handle_sub(arg1, arg2):
    if arg1 in REGISTERS and arg2 in REGISTERS:
        return 'SUB ' + REGISTERS[arg1] + ' ' + REGISTERS[arg2]
    else:
        return 'SUB 0x{:02x} 0x{:02x}'.format(arg1, arg2)


def handle_and(arg1, arg2):
    if arg1 in REGISTERS and arg2 in REGISTERS:
        return 'AND ' + REGISTERS[arg1] + ' ' + REGISTERS[arg2]
    else:
        return 'AND 0x{:02x} 0x{:02x}'.format(arg1, arg2)


def handle_or(arg1, arg2):
    if arg1 in REGISTERS and arg2 in REGISTERS:
        return 'OR ' + REGISTERS[arg1] + ' ' + REGISTERS[arg2]
    else:
        return 'OR 0x{:02x} 0x{:02x}'.format(arg1, arg2)


def handle_unk(arg1, arg2):
    if arg1 in REGISTERS and arg2 in REGISTERS:
        return 'STACK ' + REGISTERS[arg1] + ' ' + REGISTERS[arg2]
    else:
        return 'STACK 0x{:02x} 0x{:02x}'.format(arg1, arg2)


def handle_write(arg1, arg2):
    if arg1 in REGISTERS and arg2 in REGISTERS:
        return 'WRITE ' + REGISTERS[arg1] + ' ' + REGISTERS[arg2]
    else:
        return 'WRITE 0x{:02x} 0x{:02x}'.format(arg1, arg2)


def handle_read(arg1, arg2):
    if arg1 in REGISTERS and arg2 in REGISTERS:
        return 'READ ' + REGISTERS[arg1] + ' ' + REGISTERS[arg2]
    else:
        return 'READ 0x{:02x} 0x{:02x}'.format(arg1, arg2)


f = open('prog', 'rb')

program_data = f.read()

f.close()

assert len(program_data) == 1030

assert program_data[:6] == HEADER

program_code = program_data[6:606]
assert len(program_code) == 600

program_mem = program_data[0x306:]
print("-- Program Memory --")
print(program_mem)

print("-- Program Code --")

for i in range(0, 600, 3):
    op_code = OP_CODES[program_code[i+1]]
    pc = i // 3

    print("0x{:04x}".format(pc), end=' ')

    if op_code == 'SYSCALL':
        print(handle_syscall(program_code[i]))
    elif op_code == 'CND_JMP':
        print(handle_conditional_jump(struct.pack("B", program_code[i+2]), pc))
    elif op_code == 'MOV':
        print(handle_mov(program_code[i], program_code[i+2]))
    elif op_code == 'XOR':
        print(handle_xor(program_code[i], program_code[i+2]))
    elif op_code == 'CMP':
        print(handle_cmp(program_code[i], program_code[i+2]))
    elif op_code == 'ADD':
        print(handle_add(program_code[i], program_code[i+2]))
    elif op_code == 'SUB':
        print(handle_sub(program_code[i], program_code[i+2]))
    elif op_code == 'AND':
        print(handle_and(program_code[i], program_code[i+2]))
    elif op_code == 'OR':
        print(handle_or(program_code[i], program_code[i+2]))
    elif op_code == 'STACK':
        print(handle_unk(program_code[i], program_code[i+2]))
    elif op_code == 'WRITE':
        print(handle_write(program_code[i], program_code[i+2]))
    elif op_code == 'READ':
        print(handle_read(program_code[i], program_code[i+2]))
    else:
        print(OP_CODES[program_code[i+1]],
              "0x{:02x}".format(program_code[i]),
              "0x{:02x}".format(program_code[i+2]))
