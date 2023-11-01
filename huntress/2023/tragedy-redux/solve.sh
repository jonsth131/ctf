#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: $0 <file>"
    exit 1
fi

# Fix the zip header
echo -ne \\x50\\x4B\\x03\\x04\\x00\\x00\\x00\\x00 | dd conv=notrunc bs=8 count=1 of=$1

# Extract the obfuscated VBA code
APPLES=$(olevba $1 | grep "Apples =" | grep -o "[0-9]*")

# Deobfuscate the VBA code
PS=$(python3 -c "for i in range(0, len('$APPLES'), 3): print(chr(int('$APPLES'[i:i+3]) - 17), end='')")

# Extract the flag
echo $PS | cut -d' ' -f3 | base64 -d | grep -oE "flag{.*}"
