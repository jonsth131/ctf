#!/usr/bin/env python3
import re
from base64 import b64decode
from io import BytesIO
from zipfile import ZipFile

from scapy.all import IP, TCP, Raw, rdpcap


def extract_data(load):
    print("Load:", load)
    password = re.findall(r"Password: (\w+)", load)
    print("Password:", password[0])

    filenames = re.findall(r"filename\*\d=\"(.+)\"", load)
    filename = ""
    for name in filenames:
        filename += name

    print("Filename:", filename)

    filedata = re.findall(r"\"\r\nContent-ID: <.+>\r\n\r\n([\d\w\D]+)", load)[0].split(
        "\r\n"
    )

    data = (
        filedata[0]
        + filedata[1]
        + filedata[2]
        + filedata[3]
        + filedata[4]
        + filedata[5]
        + filedata[6]
    )

    if filedata[7] != "":
        data += filedata[7]

    print("Data:", data)

    raw = b64decode(data)
    file = ZipFile(BytesIO(raw))
    file.extractall(pwd=password[0].encode("utf-8"))
    file.close()


packets = rdpcap("phreaky.pcap")

load = ""
should_load = False

for packet in packets:
    if packet.haslayer(TCP) and Raw in packet and packet[IP].src == "192.168.68.108":
        p = packet[Raw].load
        if p.startswith(b"DATA"):
            should_load = True
        if p.startswith(b"QUIT"):
            extract_data(load)
            load = ""
            should_load = False
        if should_load:
            load += p.decode("utf-8")
