#!/usr/bin/env python3

import sys
import re


def variable_pass(data):
    sets = []
    return_data = []
    for line in data.split('\n'):
        if line.startswith('set ') and '%' not in line:
            sets.append(line)
        else:
            return_data.append(line)

    return_data = '\n'.join(return_data)

    if not sets:
        return return_data

    for line in sets:
        match = re.match(r'set (\w+)=(.*)', line)
        variable = f'%{match.group(1)}%'
        value = match.group(2)
        return_data = re.sub(variable, value, return_data)

    return variable_pass(return_data)


def exitcode_pass(data):
    sets = []
    return_data = []

    set_line = None

    for line in data.split('\n'):
        if line.startswith('set /a'):
            set_line = line
        elif line.startswith('cmd'):
            continue
        elif line.endswith('%=exitcodeAscii%'):
            match = re.match(r'set (\w+)=.*', line)
            variable = f'%{match.group(1)}%'
            match = re.match(r'set \/a \w+=(\d+) %% (\d+)', set_line)
            value = chr(int(match.group(1)) % int(match.group(2)))
            sets.append((variable, value))
            set_line = None
        else:
            return_data.append(line)

    return_data = '\n'.join(return_data)
    for variable, value in sets:
        return_data = re.sub(variable, value, return_data)

    return return_data


def get_flag(data):
    flag_data = []
    for line in data.split('\n'):
        if line.startswith(':: set flag_character'):
            flag_data.append(line)

    flag = [None for _ in range(len(flag_data))]

    for line in flag_data:
        match = re.match(r':: set flag_character(\d+)=(.)', line)
        flag[int(match.group(1))-1] = match.group(2)

    return ''.join(flag)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: solve.py <file>')
        sys.exit(1)

    with open(sys.argv[1], 'r') as f:
        data = f.read()

    data = variable_pass(data)
    data = exitcode_pass(data)
    flag = get_flag(data)

    print(f'Flag: {flag}')

    sys.exit(0)
