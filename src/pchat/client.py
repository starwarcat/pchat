#! /usr/bin/env python

import socket

if __name__=='__main__':
    c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    c.connect(("127.0.0.1", 8888))
    
    while True:
        msg = raw_input(":")
        c.sendall(msg)
    
    c.close()