#! usr/bin/env python

import socket


def run_server():
    server_socket = socket.socket(socket.AF_INET,
                                  socket.SOCK_STREAM,
                                  socket.IPPROTO_IP)
    server_socket.bind(("127.0.0.1", 50000))
    server_socket.listen(1)
    while True:
        conn, addr = server_socket.accept()
        message = conn.recv(1024)
        conn.sendall(message)
        conn.close()
    server_socket.close()
