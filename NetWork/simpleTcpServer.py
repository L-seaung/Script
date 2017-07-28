#!/usr/bin/env python
# -*- coding:utf-8 -*-
import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip, bind_port))

server.listen(5)

def handler_client(socket_client):
    request = socket_client.recv(1024)

    print "[*] Received:%s"% request

    socket_client.send("ACK!")

    socket_client.close()

while True:
    client, address = server.accept()

    print "[*] accepted connection from: %s:%d" % (address[0], address[1])

    client_handler = threading.Thread(target=handler_client, args=(client,))
    client_handler.start()
