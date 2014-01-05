import socket
import threading
import re
#import Tkinter

def ser():
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind(('',33333))
    s.listen(1)
    conn,addr=s.accept()
    while True:
        print '[%s:%d] send a message to me: %s'%(addr[0],addr[1],conn.recv(1024))
    s.close()

def clt():
    c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    ip_pattern=re.compile(r'^(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\.(\d{1,2}|1\d\d|2[0-4]\d|25[0-5])$')
    while True:
        ip=raw_input('Input the Server\'s IPv4 address:')
        ip_match=ip_pattern.match(ip)
        if ip_match:
            break
    c.connect((ip,33333))
    while True:
        sms=raw_input('Input the message you want to send:')
        c.sendall(sms)
    c.close()

if __name__=="__main__":
    ser=threading.Thread(target=ser)
    clt=threading.Thread(target=clt)
    ser.start()
    clt.start()
    ser.join()
    clt.join()