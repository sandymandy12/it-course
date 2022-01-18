#!/usr/bin/python3

import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 444
clientsocket.connect((host, port))

message = clientsocket.recv(1024)  # max data client accepts at once

clientsocket.close()

print(message.encode())
