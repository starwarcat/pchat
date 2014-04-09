import socket
import thread
from collections import deque
import sys

class serv():
    
    #initial parameter
    HOST = None
    PORT = None
    ADDRESS = (HOST,PORT)
    CLIENT_LIST = {}
    MAX_CONN = 99
    MESSAGE_QUEUE = deque([])

    def __init__(self):
        self.HOST = sys.argv[1]
        self.PORT = int(sys.argv[2])
        self.ADDRESS = (self.HOST,self.PORT)

    def serv_proc(self):
        self.serv_send_thread()
        print self.ADDRESS
        l_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        l_socket.bind((self.HOST,self.PORT))
        l_socket.listen(self.MAX_CONN)
        while True:
            (conn, c_addr) = l_socket.accept()
            (CLIENT_HOST,CLIENT_PORT) = c_addr
            _thread = thread.start_new_thread(self.serv_recv,(conn,c_addr))

    def serv_recv(self,__CONN,__ADDRESS):
        self.CLIENT_LIST[__ADDRESS] = __CONN
        print 'LIST: ',self.CLIENT_LIST.keys()
        (CLIENT_HOST,CLIENT_PORT) = __ADDRESS
        while True:
            recv_data = __CONN.recv(1024)
            if not recv_data: break
            self.MESSAGE_QUEUE.append(recv_data)
        __CONN.close()
        del self.CLIENT_LIST[__ADDRESS]

    def serv_send(self):
        while True:
            if self.MESSAGE_QUEUE:
                recv_data = self.MESSAGE_QUEUE.popleft()
                for _conn in self.CLIENT_LIST.values():
                    _conn.sendall(recv_data)

    def serv_send_thread(self):
        thread.start_new_thread(self.serv_send,())



if __name__ == '__main__':
    if len(sys.argv) != 3 :
        print 'giving host ip, port to start Pchat server...'
        print 'Usage:'
        print 'python serv.py 192.168.153.128 5678'
        sys.exit()
    print "Pchat server starting..."
    l = serv()
    l.serv_proc()


