#!/usr/bin/python3

import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# host can be manually set
host = socket.gethostname()  # ip address of server, could have issues
port = 444

serversocket.bind((host, port))

serversocket.listen(3)

while True:
    clientsocket, address = serversocket.accept()
    print('recieved connection from ' % str(address))

    message = 'Connected to server' + "\r\n"

    clientsocket.send(message)
    clientsocket.close()
