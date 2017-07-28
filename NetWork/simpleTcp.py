#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket

target_host = "www.baidu.com"
target_port = 80

def client():
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client.connect((target_host, target_port))

    client.send("GET /HTTP/1.1\r\t\nHost:baidu.com\r\t\n")

    response = client.recv(4096)

    print response

def main():
    client()

if __name__ == '__main__':
    main()
