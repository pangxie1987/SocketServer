#-*- coding:utf-8 -*-
'''
创建UDPServer
'''
from socketserver import BaseRequestHandler,ThreadingUDPServer,UDPServer
import time

class TimeHandler(BaseRequestHandler):
    def handle(self):
        print('Got connection from ',self.client_address)
        msg,sock=self.request
        resp=time.ctime()
        sock.sendto(resp.encode('ascii'),self.client_address)

if __name__=='__main__':
    
    # #单线程模式（一次只能响应一个连接请求）
    # serv=UDPServer(('',20000),TimeHandler)

    #多线程模式（响应多个客户端的连接）
    serv=ThreadingUDPServer(('',20000),TimeHandler)
    serv.serve_forever()