# -*- coding:utf-8 -*-
'''
创建一个能接受客户的消息，在消息前加一个时间戳后返回的TCP服务器
socket:套接字
AF_INET:socket网络编程
SOCK_STREAM:TCP/IP
'''
from socket import socket, AF_INET, SOCK_STREAM
from time import ctime


host = ''
port = '62555'
addr = (host, port) # host为空表示监听任意IP的连接请求

s = socket(AF_INET, SOCK_STREAM)
s.bind(addr)
s.listen(5)  # listen()参数表示最多运行几个连接同时连进来，后来的连接就会被拒绝掉

while True:
    print('wating for connecting...')
    tcpCliSock, addr = s.accept()
    print('connected from ',addr)

    while True:
        data = tcpCliSock.recv(1024)  #接收消息的长度
        print('data:',data)
        if not data:
            break
        tcpCliSock.send('[%s] %s'%(ctime(), data))

    tcpCliSock.close()
s.close()
