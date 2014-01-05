# _*_ coding:utf-8 _*_
# Filename:ServerUI.py
# Python在线聊天服务器端
# Modified by validboy 0104
 
import Tkinter
import tkFont
import socket
import thread
import time
import sys
 
class ServerUI():
     
    title = 'Python在线聊天-服务器端V1.0'
    local = '127.0.0.1'
    port = 8808
    global serverSock;
    flag = False
     
    
#初始化类的相关属性，类似于Java的构造方法
    def __init__(self):
        self.root = Tkinter.Tk()
        self.root.title(self.title)
         
        
#窗口面板,用4个frame面板布局
        self.frame = [Tkinter.Frame(),Tkinter.Frame(),Tkinter.Frame(),Tkinter.Frame()]
 
        
#显示消息Text右边的滚动条
        self.chatTextScrollBar = Tkinter.Scrollbar(self.frame[0])
        self.chatTextScrollBar.pack(side=Tkinter.RIGHT,fill=Tkinter.Y)
         
        
#显示消息Text，并绑定上面的滚动条
        ft = tkFont.Font(family='Fixdsys',size=11)
        self.chatText = Tkinter.Listbox(self.frame[0],width=70,height=18,font=ft)
        self.chatText['yscrollcommand'] = self.chatTextScrollBar.set
        self.chatText.pack(expand=1,fill=Tkinter.BOTH)
        self.chatTextScrollBar['command'] = self.chatText.yview()
        self.frame[0].pack(expand=1,fill=Tkinter.BOTH)
         
        
#标签，分开消息显示Text和消息输入Text
        label = Tkinter.Label(self.frame[1],height=2)
        label.pack(fill=Tkinter.BOTH)
        self.frame[1].pack(expand=1,fill=Tkinter.BOTH)
         
        
#输入消息Text的滚动条
        self.inputTextScrollBar = Tkinter.Scrollbar(self.frame[2])
        self.inputTextScrollBar.pack(side=Tkinter.RIGHT,fill=Tkinter.Y)
         
        
#输入消息Text，并与滚动条绑定
        ft = tkFont.Font(family='Fixdsys',size=11)
        self.inputText = Tkinter.Text(self.frame[2],width=70,height=8,font=ft)
        self.inputText['yscrollcommand'] = self.inputTextScrollBar.set
        self.inputText.pack(expand=1,fill=Tkinter.BOTH)
        self.inputTextScrollBar['command'] = self.chatText.yview()
        self.frame[2].pack(expand=1,fill=Tkinter.BOTH)
         
        
#发送消息按钮
        self.sendButton=Tkinter.Button(self.frame[3],text=' 发 送 ',width=10,command=self.sendMessage)
        self.sendButton.pack(expand=1,side=Tkinter.BOTTOM and Tkinter.RIGHT,padx=25,pady=5)
 
        
#关闭按钮
        self.closeButton=Tkinter.Button(self.frame[3],text=' 关 闭 ',width=10,command=self.close)
        self.closeButton.pack(expand=1,side=Tkinter.RIGHT,padx=25,pady=5)
        self.frame[3].pack(expand=1,fill=Tkinter.BOTH)
         
    
#接收消息
    def receiveMessage(self):
        
#建立Socket连接
        self.serverSock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.serverSock.bind((self.local,self.port))
        self.serverSock.listen(15)
        self.buffer = 1024
        self.chatText.insert(Tkinter.END,'服务器已经就绪......')
        
#循环接受客户端的连接请求
        while True:
            self.connection,self.address = self.serverSock.accept()
            self.flag = True
            while True:
                
#接收客户端发送的消息
                self.cientMsg = self.connection.recv(self.buffer)
                if not self.cientMsg:
                    continue
                elif self.cientMsg == 'Y':
                    self.chatText.insert(Tkinter.END,'服务器端已经与客户端建立连接......')
                    self.connection.send('Y')
                elif self.cientMsg == 'N':
                    self.chatText.insert(Tkinter.END,'服务器端与客户端建立连接失败......')
                    self.connection.send('N')
                else:
                    theTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                    self.chatText.insert(Tkinter.END, '客户端 ' + theTime +' 说：\n')
                    self.chatText.insert(Tkinter.END, '  ' + self.cientMsg)
     
    
#发送消息
    def sendMessage(self):
        
#得到用户在Text中输入的消息
        message = self.inputText.get('1.0',Tkinter.END)
        
#格式化当前的时间
        theTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        self.chatText.insert(Tkinter.END, '服务器 ' + theTime +' 说：\n')
        self.chatText.insert(Tkinter.END,'  ' + message + '\n')
        if self.flag == True:
            
#将消息发送到客户端
            self.connection.send(message)
        else:
            
#Socket连接没有建立，提示用户
            self.chatText.insert(Tkinter.END,'您还未与客户端建立连接，客户端无法收到您的消息\n')
        
#清空用户在Text中输入的消息
        self.inputText.delete(0.0,message.__len__()-1.0)
     
    
#关闭消息窗口并退出
    def close(self):
        sys.exit()
     
    
#启动线程接收客户端的消息
    def startNewThread(self):
        
#启动一个新线程来接收客户端的消息
        
#thread.start_new_thread(function,args[,kwargs])函数原型，
        
#其中function参数是将要调用的线程函数，args是传递给线程函数的参数，它必须是个元组类型，而kwargs是可选的参数
        
#receiveMessage函数不需要参数，就传一个空元组
        thread.start_new_thread(self.receiveMessage,())
     
def main():
    server = ServerUI()
    server.startNewThread()
    server.root.mainloop()
     
if __name__=='__main__':
    main()
