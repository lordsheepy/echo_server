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
        message = recv_data(conn)
        conn.sendall(message)
        conn.close()

    server_socket.close()


def recv_data(conn):
    message = ''
    while True:
        message += conn.recv(32)
        if not conn.recv(32):
            return message


if __name__ == '__main__':
    run_server()
