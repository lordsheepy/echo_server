#! usr/bin/env python

import socket


def run_server():
    server_socket = socket.socket(socket.AF_INET,
                                  socket.SOCK_STREAM,
                                  socket.IPPROTO_IP)
    server_socket.bind(("127.0.0.1", 50000))
    server_socket.listen(1)
    conn, addr = server_socket.accept()
    while True:
        message = conn.recv(1024)
        if not message:
            break
        conn.sendall(message)
    conn.close()
    server_socket.close()


def start_server():
    while True:
        run_server()
