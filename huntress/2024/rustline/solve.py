#!/usr/bin/env python3
import re

enc_data = open("encrypted-files/id_rsa_aws_ec2", "rb").read()
orig_data = open("challenge-files/id_rsa_aws_ec2", "rb").read()

key = [orig_data[i] ^ enc_data[i] for i in range(len(orig_data))]

enc_flag = open("encrypted-files/flag.txt", "rb").read()

flag = bytes([enc_flag[i] ^ key[i % len(key)]
             for i in range(len(enc_flag))]).decode()

flag = re.findall(r"flag{.*?}", flag)[0]

print(flag)
