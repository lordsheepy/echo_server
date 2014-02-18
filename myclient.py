#! usr/bin/env python

import socket


def start_client(message):
    client_socket = socket.socket(socket.AF_INET,
                                  socket.SOCK_STREAM,
                                  socket.IPPROTO_IP)
    client_socket.connect(('127.0.0.1', 50000))
    client_socket.sendall(message)
    client_socket.shutdown(socket.SHUT_WR)
    response = client_socket.recv(1024)
    client_socket.close()
    return response
