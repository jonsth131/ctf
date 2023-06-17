#!/bin/bash
# Dependencies: apktool, python3

apktool d fortune_teller.apk

python3 decrypt.py

rm -rf fortune_teller

echo "Flag in decrypted.jpg"
