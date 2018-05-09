# -*- coding:utf-8 -*-
'''
UDP Client
'''

from socket import socket,AF_INET,SOCK_DGRAM
s=socket(AF_INET,SOCK_DGRAM)
s.sendto(b'',('localhost',20000))

print(s.recv(1024))