# import socket               # Import socket module
#
# soc = socket.socket()         # Create a socket object
# host = "localhost" # Get local machine name
# port = 2004                # Reserve a port for your service.
# soc.bind((host, port))       # Bind to the port
# soc.listen(5)                 # Now wait for client connection.
# while True:
#     conn, addr = soc.accept()     # Establish connection with client.
#     print ("Got connection from",addr)
#     msg = conn.recv(1024)
#     print (msg)
#     if ( msg[2:] == b"Hello Server" ):
#         print("Hii everyone")
#     else:
#         print("Go away")



# Above is how to set up server on local host.
from googlesearch import search
import socket
import numpy
import os
import sys

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 2004
soc.bind((host, port))
soc.listen(5)
while True:
    conn, addr = soc.accept()
    print("Got connection from", addr)
    x = conn.recv(1024)
    print(x)
    for j in search(x, tld="co.in", num=10, stop=10, pause=2):
        print(j)
