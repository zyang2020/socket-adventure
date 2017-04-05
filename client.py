import socket
import sys

try:
    port = int(sys.argv[1])
except IndexError:
    print("Please include a port number, eg: python serve.py 50000")
    exit(-1)

client_socket = socket.socket()
client_socket.connect(("127.0.0.1", port))

while True:
    response = client_socket.recv(4096).decode()
    print(response)

    if response == "":
        break

    my_message = input("> ").encode('utf-8')
    client_socket.sendall(my_message)
