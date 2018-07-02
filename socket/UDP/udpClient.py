# -*- coding:utf-8 -*-
'''
创建一个UDP客户端，发送消息并接收服务器返回的带时间戳的消息
'''

from socket import socket, AF_INET, SOCK_DGRAM

host = '127.0.0.1'
port = 62555
addr = (host, port)

s = socket(AF_INET, SOCK_DGRAM)
# udp无connect()

while True:
    try:
        input = raw_input('>')
        if not input:
            break
        s.sendto(input, addr)
        data, addr = s.recvfrom(1024)
        if not data:
            break
        print(data)
    except KeyboardInterrupt:
        s.close()