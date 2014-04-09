import socket
import thread
import sys
import curses

class client():

    #initial parameter
    HOST = None
    PORT = None
    ADDRESS = None
    c_socket = None
    CHATNAME = None
    stdscr = None
    BOLD = '\033[1m'
    FG_BLUE = '\033[34m'
    END = "\033[0;0m"

    def __init__(self):
        self.HOST = sys.argv[1]
        self.PORT = int(sys.argv[2])
        self.CHATNAME = sys.argv[3]
        self.ADDRESS = (self.HOST,self.PORT)
#        self.stdscr = curses.initscr()
#       curses.start_color()
#       curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_BLACK)
        

    def client_console (self):
        self.c_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.c_socket.connect(self.ADDRESS)
        self.client_recv_thread()
        while True:
            send_data = raw_input()
            if str(send_data) == 'exit':
                print "Bye..."
                break
            if str(send_data) == '':
                continue
            send_data = self.CHATNAME + ': ' + send_data
            self.c_socket.sendall(send_data)
        self.c_socket.close()


    def client_recv(self):
        while True:
            recv_data = self.c_socket.recv(1024)
            if recv_data.startswith(self.CHATNAME):
                continue
            print self.BOLD + self.FG_BLUE + str(recv_data) + self.END
#            recv_data = recv_data + '\n'
#           self.stdscr.addstr(recv_data, curses.A_BOLD|curses.color_pair(1))
#           self.stdscr.refresh()
            

    def client_recv_thread(self):
        thread.start_new_thread(self.client_recv,())            


if __name__ == '__main__':
    if len(sys.argv) != 4 :
        print 'giving host ip, port and a nickname to start chatting...'
        print 'Usage:'
        print 'python client.py 192.168.153.128 5678 Mylord'
        print 'python client.py 192.168.153.128 5678 YourAssistant'
        sys.exit()
    print 'Starting Pchat...'
    print 'type exit to leave...'
    c = client()
    c.client_console()

