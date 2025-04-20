#!/usr/bin/python3
import socket
import sys
host = "127.0.0.1"
port = 1234

# create a socket object
# Using standard IPv4 address or hostname by AF_INET
# SOCK_STREAM indicates this will be a TCP client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Now connect the client
client.connect((host, port))

# receive some data from the client
response = client.recv(4096)

print(response)
client.close()
# Finally close socket
