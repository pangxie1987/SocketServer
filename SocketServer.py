# # -*- coding:utf-8 -*-

'''
使用socketserver创建一个TCP服务器

'''
from socketserver import BaseRequestHandler,TCPServer,ThreadingTCPServer
from socket import  socket,AF_INET,SOCK_STREAM

class EchoHandler(BaseRequestHandler):
        
    def handle(self):
        print('Got connection from ',self.client_address)
        
        while True:

            msg=self.request.recv(1024)
            if not msg:
                break
            self.request.send(msg)
            print(msg)

if __name__=='__main__':
    '''
    ##单个客户端连接
    # serv=TCPServer(('',20000),EchoHandler)    #单个客户端连接
    # serv.serve_forever()
    '''
    '''
    ##多个客户端连接
    # serv=ThreadingTCPServer(('',20000),EchoHandler)  #多个客户端连接
    # serv.serve_forever()
    '''

    '''
    #穿件线程池，控制连接数
    from threading import Thread
    NWORKS=2
    serv=TCPServer(('',20000),EchoHandler)
    for n in range(NWORKS):
        t=Thread(target=serv.serve_forever)
        t.daemon=True
        t.start()
    serv.serve_forever()
    '''

    
    # 设置socket参数
    # SOL_SOCKET 
    from socket import SOL_SOCKET,SO_REUSEADDR

    serv=TCPServer(('',20000),EchoHandler,bind_and_activate=False)

    
    # 设置scoket的level，选择SOL_SOCKET，值为SO_REUSEADDR
    # SO_REUSEADDR当socket关闭后，本地端用于该socket的端口号立刻就可以被重用。
    # 通常来说，只有经过系统定义一段时间后，才能被重用。
    serv.socket.setsockopt(SOL_SOCKET,SO_REUSEADDR,True)

    # serv.bind(host,port)
    # 将套接字绑定到地址, 在AF_INET下,以元组（host,port）的形式表示地址.
    serv.server_bind()

    # 通过服务器的构造函数来激活服务器。默认的行为只是监听服务器套接字。可重载。
    serv.server_activate()

    serv.serve_forever()