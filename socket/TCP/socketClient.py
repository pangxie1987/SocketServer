# -*- coding:utf-8 -*-
'''
创建一个TCP客户端，程序会提示用户输入要传给服务器的信息，显示服务器返回的加了时间戳的结果
'''

from socket import socket, AF_INET, SOCK_STREAM
import time

s = socket(AF_INET, SOCK_STREAM)
s.connect(('127.0.0.1', 62555))

while True:
    try:
        input = raw_input('>')
        if not input:
            break
        s.send(input)
        data = s.recv(1024)
        if not data:
            break
        print(data)

        time.sleep(1)
    except KeyboardInterrupt as e:
        # pass 
        print('close connecting...')
        s.close()
        break
        

    