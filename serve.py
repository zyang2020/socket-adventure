import sys

from server import Server

try:
    port = int(sys.argv[1])
except IndexError:
    print("Please include a port number, eg: python serve.py 50000")
    exit(-1)

server = Server(port)
server.serve()
