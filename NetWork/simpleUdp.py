#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket

target_host = "127.0.0.1"
target_port = 80

def udpClient():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    client.send("AAAAABBBBBCCCC", (target_host, target_port))

    data, address = client.recvfrom(4096)

    print data, address

def main():
    udpClient()

if __name__ == '__main__':
    main()
    
