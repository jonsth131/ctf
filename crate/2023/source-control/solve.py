#!/usr/bin/env python3
import socket

HOST = "challs.crate.nu"
PORT = 24924


def main():
    print("Connecting to {}:{}".format(HOST, PORT))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    data = s.recv(1024).decode()
    s.close()

    new_port = int(data.split("on the port ")[1].split(".")[0])
    source_port = int(data.split("from the port ")[1].split(".")[0])
    message = data.split("\n")[-2]

    print("New port: {}".format(new_port))
    print("Source port: {}".format(source_port))
    print("Message: {}".format(message))

    print("Connecting to {}:{}".format(HOST, new_port))
    print("Using source port {}".format(source_port))
    s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s2.bind(("0.0.0.0", source_port))
    s2.connect((HOST, new_port))
    s2.send(message.encode())
    print("Sent message!")
    data = s2.recv(1024)
    s2.close()
    print("Received data: {}".format(data.decode()))


if __name__ == "__main__":
    main()
