#! usr/bin/env python

"""Sends string to echo server with command line arg"""

import socket
import sys
import mysocket


def start_client(message):
    client_socket = socket.socket(socket.AF_INET,
                                  socket.SOCK_STREAM,
                                  socket.IPPROTO_IP)
    client_socket.connect(('127.0.0.1', 50000))
    client_socket.sendall(message)
    client_socket.shutdown(socket.SHUT_WR)
    response = mysocket.recv_data(client_socket)
    client_socket.close()
    return response


if __name__ == '__main__':
    message = sys.argv[1]  # takes commandline argument
    print(start_client(message))
