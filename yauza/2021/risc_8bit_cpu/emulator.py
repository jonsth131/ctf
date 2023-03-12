#!/usr/bin/env python3
import struct

DEBUG = False

STATE = {
    'PC': 0x1000,
    'FLAG_REGISTER': False,
    'REGISTERS': {
        0: 0,
        1: 0,
        2: 0,
    }
}

SERIAL_OUT = bytearray()

def debug(*args):
    if DEBUG == True:
        print(args)

def read_file(name):
    try:
        fh = open(name, 'rb')
        data = fh.read()
        fh.close()
        return bytearray(data)
    except:
        print('Could not read rom from', name)
        exit(-1)


MEMORY = read_file('rom.bin')


def get_register_addr():
    REGISTERS = STATE['REGISTERS']
    addr = bytearray()
    addr.append(REGISTERS[1])
    addr.append(REGISTERS[2])
    int_addr = struct.unpack('>H', addr)
    return int_addr[0]


def add_op(data):
    REGISTERS = STATE['REGISTERS']
    if data[0] in REGISTERS:
        debug('add', data[0], data[2])
        REGISTERS[data[0]] += data[2]
        REGISTERS[data[0]] &= 0xff


def xor_op(data):
    REGISTERS = STATE['REGISTERS']
    if data[0] in REGISTERS:
        debug('xor', hex(REGISTERS[data[0]]), (data[2]))
        REGISTERS[data[0]] = REGISTERS[data[0]] ^ data[2]
        REGISTERS[data[0]] &= 0xff


def and_op(data):
    REGISTERS = STATE['REGISTERS']
    if data[0] in REGISTERS:
        debug('and', hex(REGISTERS[data[0]]), (data[2]))
        REGISTERS[data[0]] = REGISTERS[data[0]] & data[2]
        REGISTERS[data[0]] &= 0xff


def or_op(data):
    REGISTERS = STATE['REGISTERS']
    if data[0] in REGISTERS:
        debug('or', hex(REGISTERS[data[0]]), (data[2]))
        REGISTERS[data[0]] = REGISTERS[data[0]] | data[2]
        REGISTERS[data[0]] &= 0xff


def ld_op(data):
    if data[0] in STATE['REGISTERS']:
        debug('ld', data)
        STATE['REGISTERS'][data[0]] = data[2]


def ldr_op(data):
    REGISTERS = STATE['REGISTERS']
    if data[0] in REGISTERS:
        int_addr = get_register_addr()
        debug('ldr', hex(int_addr), hex(MEMORY[int_addr]))
        REGISTERS[data[0]] = MEMORY[int_addr]


def ldr_kk_op(data):
    REGISTERS = STATE['REGISTERS']
    if data[0] in REGISTERS:
        addr = bytearray()
        addr.append(data[1])
        addr.append(data[2])
        int_addr = struct.unpack('>H', addr)
        int_addr = int_addr[0]
        debug('ldrkk', hex(int_addr), hex(MEMORY[int_addr]))
        REGISTERS[data[0]] = MEMORY[int_addr]


def str_op(data):
    REGISTERS = STATE['REGISTERS']
    if data[0] in REGISTERS:
        int_addr = get_register_addr()
        debug('str', hex(int_addr), hex(REGISTERS[data[0]]))
        MEMORY[int_addr] = REGISTERS[data[0]]

def str_kk_op(data):
    REGISTERS = STATE['REGISTERS']
    if data[0] in REGISTERS:
        addr = bytearray()
        addr.append(data[1])
        addr.append(data[2])
        int_addr = struct.unpack('>H', addr)
        int_addr = int_addr[0]
        debug('strkk', hex(int_addr), hex(REGISTERS[data[0]]))
        MEMORY[int_addr] = REGISTERS[data[0]]


def jmp_op(data):
    addr = bytearray()
    addr.append(data[1])
    addr.append(data[2])
    int_addr = struct.unpack('>H', addr)
    int_addr = int_addr[0]
    debug('JMP', hex(int_addr))
    debug(hex(STATE['PC']))
    STATE['PC'] = int_addr
    debug(hex(STATE['PC']))


def jnz_op(data):
    if STATE['FLAG_REGISTER'] == False:
        addr = bytearray()
        addr.append(data[1])
        addr.append(data[2])
        int_addr = struct.unpack('>H', addr)
        int_addr = int_addr[0]
        debug('jnz', hex(int_addr))
        debug(hex(STATE['PC']))
        STATE['PC'] = int_addr
        debug(hex(STATE['PC']))


def cmpeq_op(data):
    REGISTERS = STATE['REGISTERS']
    if data[0] in REGISTERS:
        if REGISTERS[data[0]] == data[2]:
            STATE['FLAG_REGISTER'] = True
        else:
            STATE['FLAG_REGISTER'] = False

        debug('cmpeq', REGISTERS[data[0]], data[2], STATE['FLAG_REGISTER'])


def mov_op(data):
    REGISTERS = STATE['REGISTERS']
    if data[0] in REGISTERS and data[2] in REGISTERS:
        debug('MOV', REGISTERS[data[0]], REGISTERS[data[2]])
        STATE['REGISTERS'][data[0]] = STATE['REGISTERS'][data[2]]


def hlt_op(data):
    return 'HLT'


def nop_op(data):
    debug('nop')
    return

def put_op(data):
    REGISTERS = STATE['REGISTERS']
    if data[0] in REGISTERS:
        SERIAL_OUT.append(REGISTERS[data[0]])

OPCODES = {
    0x00: add_op,
    0x01: xor_op,
    0x02: and_op,
    0x03: or_op,
    0x04: ld_op,
    0x05: mov_op,
    0x06: ldr_kk_op,
    0x07: ldr_op,
    0x08: str_kk_op,
    0x09: str_op,
    0x0a: put_op,
    0x0b: jmp_op,
    0x0c: jnz_op,
    0x0e: cmpeq_op,
    0x44: hlt_op,
    0x33: nop_op,
}


def run():
    while STATE['PC'] < len(MEMORY):
        opcode = MEMORY[STATE['PC']]
        debug(MEMORY[STATE['PC']:STATE['PC']+4])
        if opcode in OPCODES:
            func = OPCODES[opcode]
            func(MEMORY[STATE['PC']+1:STATE['PC']+4])
            debug(hex(STATE['PC']), STATE['REGISTERS'])
        else:
            debug('not found opcode')

        STATE['PC'] += 4


run()

print(SERIAL_OUT.decode())
