#! usr/bin/env python

import socket
"""Simple echo server with no arguments"""


def run_server():

    server_socket = socket.socket(socket.AF_INET,
                                  socket.SOCK_STREAM,
                                  socket.IPPROTO_IP)
    server_socket.bind(("127.0.0.1", 50000))
    server_socket.listen(1)

    while True:  # endless loop to permit server to continue echo function
        conn, addr = server_socket.accept()
        message = conn.recv(32)
        conn.sendall(message)
        conn.close()

    server_socket.close()


if __name__ == '__main__':
    run_server()
