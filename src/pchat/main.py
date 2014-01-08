import socket
import thread
import time
import traceback
import sys
from server import *
  
def Go():
    server = Server()
    server.doTask()
     

######################################################################################################
    
if __name__=='__main__':  
    Go()
    
    
    
    
        