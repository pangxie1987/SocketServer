# -*- coding:utf-8 -*-
'''
用于连接TCP服务的客户端
'''


from socket import  socket,AF_INET,SOCK_STREAM

s=socket(AF_INET,SOCK_STREAM)

s.connect(('localhost',20000))
while True:
    msg=(input(">>:").strip()).encode('utf-8')
    if len(msg)==0:
        continue
    elif msg==b'exit':
        break
    s.sendall(msg)
    data=s.recv(1024)
    print('Received:',data)

s.close()
        
# print(s.send(b'hello'))
# print(s.recv(8192))