#!/usr/bin/env python3

data = [
    "10.25.3.103",
    "10.5.13.54",
    "10.185.7.102",
    "172.21.29.54",
    "172.20.20.51",
    "172.30.27.54",
    "192.168.34.57",
    "192.168.71.6",
    "10.76.2.97",
    "10.199.9.97",
    "192.168.245.16",
    "172.25.31.54",
    "192.168.226.0",
    "10.215.6.57",
    "192.168.41.1",
    "10.212.10.49",
    "10.119.16.50",
    "10.0.0.102",
    "172.30.21.57",
    "192.168.43.2",
    "192.168.113.16",
    "172.26.24.100",
    "192.168.89.12",
    "172.21.33.101",
    "192.168.37.125",
    "172.17.19.49",
    "10.169.8.52",
    "10.179.4.123",
    "172.29.22.50",
    "192.168.180.8",
    "172.28.26.97",
    "172.24.23.50",
    "192.168.40.18",
    "172.16.30.98",
    "10.13.1.108",
    "192.168.42.0",
    "172.16.17.102",
    "10.105.11.55",
    "192.168.36.49",
    "172.30.18.56",
    "172.24.25.99",
    "192.168.100.12",
    "192.168.35.97",
    "172.30.28.99",
    "172.27.32.53",
    "192.168.58.18",
    "10.184.15.101",
    "192.168.50.15",
    "10.129.5.53",
    "10.126.12.98",
    "10.32.14.57",
]
flag = [None] * 38
for ip in data:
    ip = ip.split(".")
    if int(ip[2]) < len(flag):
        flag[int(ip[2])] = chr(int(ip[3]))

print("".join(flag))
