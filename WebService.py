#-*- coding:utf-8 -*-
'''
模拟WEB服务器
'''


from socket import socket,AF_INET,SOCK_STREAM

def handle_request(client):
    buff=client.recv(1024)
    print(buff)
    client.sendall(b'HTTP/1.1 200 OK\r\n\r\n')
    client.sendall(b'Hello,World!')


def main():
    serv=socket(AF_INET,SOCK_STREAM)
    serv.bind(('localhost',8001))
    serv.listen(5)
    print('Waiting for connection...')
    
    while True:
        connection,address=serv.accept()
        print('Got connection form ',address)
        handle_request(connection)
        connection.close()

if __name__=='__main__':
    main()