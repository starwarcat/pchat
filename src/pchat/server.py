import socket
import thread
import time
import traceback
import sys

class Server():
    
    login_socket = None
    host = "127.0.0.1"
    port = 8888
    
    def __init__(self):
        self.login_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.login_socket.bind((self.host, self.port))
        self.login_socket.listen(99)
  
    def doTask(self):
        
        while True:
            try:
                print 'Waiting for Login...'
                self.conn, self.addr = self.login_socket.accept()
                
                print self.addr[0], self.addr[1]
                print 'Got 1 connection...'
                
                while True:
                    msg = self.conn.recv(1024)
                    if not msg:
                        print "Disconnected..."
                        break
                    print msg
                
            except Exception as e:
                print "Unexpected error:", sys.exc_info()[0]    
    
    
    
    
        