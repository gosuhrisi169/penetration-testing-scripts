# Import the socket library
import socket

# create a socket object
s = socket.socket()
print("Socket successfully created")

# reserve the port on your computer. in this case it is 1234 but it can be anything
port = 1234

# Bind to the port
# we have not typed any ip in the ip field instead we have inputted an empty string this makes the server listen to requests coming from other computers on the network

s.bind(('', port))
print("socket binded to %s" % (port))

# put the socket into listening mode
s.listen(5)
print("socket is listening")

# running forever loop until we interrupt it or an error occurs
while True:

    # Establishing connection with client.
    c, addr = s.accept()
    print('Got connection from', addr)

    # sending a thank you message to the client.
    c.send(b'Thank you for connecting')

    # Finally closing the connection with the client
    c.close()
