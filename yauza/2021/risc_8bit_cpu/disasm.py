#!/usr/bin/env python3

START_ADDR = 0x1000

def rx(op, data):
    if data[0] in REGISTERS:
        return f'{op} {REGISTERS[data[0]]}'
    else:
        return 'INVALID'

def rxkk(op, data):
    if data[0] in REGISTERS:
        return f'{op} {REGISTERS[data[0]]} {hex(data[2])}'
    else:
        return 'INVALID'

def rxkkkk(op, data):
    if data[0] in REGISTERS:
        return f'{op} {REGISTERS[data[0]]} {data[1:3]}'
    else:
        return 'INVALID'

def kkkk(op, data):
    return f'{op} {data[1:3]}'

def add_op(data):
    return rxkk('ADD', data)

def xor_op(data):
    return rxkk('XOR', data)

def and_op(data):
    return rxkk('AND', data)

def or_op(data):
    return rxkk('OR', data)

def ld_op(data):
    return rxkk('LD', data)

def mov_op(data):
    return f'MOV {REGISTERS[data[0]]} {REGISTERS[data[2]]}'

def ldr_adr_op(data):
    return rxkkkk('LDR', data)

def ldr_op(data):
    return rx('LDR', data)

def str_adr_op(data):
    return rxkkkk('STR', data)

def str_op(data):
    return rx('STR', data)

def put_op(data):
    return rx('PUT', data)

def jmp_op(data):
    return kkkk('JMP', data)

def jnz_op(data):
    return kkkk('JNZ', data)

def jz_op(data):
    return kkkk('JZ', data)

def cmpeq_op(data):
    return rxkk('CMPEQ', data)

def hlt_op(data):
    return 'HLT'

def nop_op(data):
    return 'NOP'

OPCODES = {
    0x00: add_op,
    0x01: xor_op,
    0x02: and_op,
    0x03: or_op,
    0x04: ld_op,
    0x05: mov_op,
    0x06: ldr_adr_op,
    0x07: ldr_op,
    0x08: str_adr_op,
    0x09: str_op,
    0x0a: put_op,
    0x0b: jmp_op,
    0x0c: jnz_op,
    0x0d: jz_op,
    0x0e: cmpeq_op,
    0x44: hlt_op,
    0x33: nop_op,
}

REGISTERS = {
    0: 'A',
    1: 'B',
    2: 'C',
}


def add(data):
    return f'ADD {REGISTERS[data[0]]} {data[2]}'



def read_file(name):
    try:
        fh = open(name, 'rb')
        data = fh.read()
        fh.close()
        return data
    except:
        print('Could not read data from', name)
        exit(-1)


def disassemble(data: bytes):
    index = 0
    disassembly = []
    while index < len(data):
        opcode = data[index]
        if opcode in OPCODES:
            func = OPCODES[opcode]
            disasm = func(data[index+1:index+4])
            disassembly.append(f'{hex(START_ADDR+index)}: {disasm}')

        index += 4

    return disassembly


data = read_file('rom.bin')
disassembly = disassemble(data[START_ADDR:])

fh = open('disassembly', 'w')
for line in disassembly:
    fh.write(line + '\n')
fh.close()
