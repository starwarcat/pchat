#! /usr/bin/env python

import socket
import threading

class Client():
    flag = True
    c = None
    
    def __init__(self):
        self.flag = True
        self.c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.c.connect(("127.0.0.1", 9999))
    
    def receiver(self):
        while self.flag:
            msg = self.c.recv(1024)
            if not msg:
                continue
            print ""
            print "Server say:" + msg
#         self.c.close()
        
    def sender(self):
        while self.flag:
            msg = raw_input("you:")
            if(msg == "/quit"):
                self.flag = False
            self.c.sendall(msg)
#         self.c.close()
        
if __name__=='__main__':
    client = Client()
    
    rcv = threading.Thread(target=client.receiver)
    sdr = threading.Thread(target=client.sender)
    rcv.start()
    sdr.start()
    rcv.join()
    sdr.join()
    print 'End'