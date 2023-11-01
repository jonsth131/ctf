#!/bin/bash
# Uses https://github.com/ribt/dtmf-decoder to decode the dialtone

DIALTONE=$(python3 dtmf.py dialtone.wav)

# Convert dialtone value to hex, remove the 0x prefix, and decode the hex value
python3 -c "print(bytes.fromhex(hex($DIALTONE)[2:]).decode())"

