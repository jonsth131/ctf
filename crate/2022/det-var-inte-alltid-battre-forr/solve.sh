#!/bin/bash

if [ -d "./rsa" ]; then
   echo "Keys found, skipping download"
else
   echo "Keys not found, downloading"
   wget https://hdm.io/tools/debian-openssl/debian_ssh_rsa_2048_x86.tar.bz2 -O ./rsa.tar.bz2
    tar xfvj rsa.tar.bz2
    rm rsa.tar.bz2
fi

HASH=$(ssh-keygen -E md5 -lf rsa.pub | awk -F " " '{print $2}' | cut -c5- | sed 's/://g')
KEYFILE=$(ls -lt rsa/2048/$HASH* | head -1 | awk -F " " '{print $9}')

openssl pkeyutl -inkey $KEYFILE -decrypt -in message.bin