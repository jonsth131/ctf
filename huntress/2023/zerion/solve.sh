#!/bin/bash
# This script mimics the first stage of the PHP code in zerion.
# It takes the extra data after the PHP code, reverses it, ROT13s it, and base64 decodes it.
# It then greps for the flag in the resulting decoded script.

cat zerion | cut -d ">" -f 2 | rev | tr 'A-Za-z' 'N-ZA-Mn-za-m' | base64 -d | grep -oE "flag{.*}"
