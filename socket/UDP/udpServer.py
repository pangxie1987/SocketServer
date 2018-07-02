'''
UDPSERVER  接收客户端的消息，在消息前加一个时间戳返回的UDP服务器
'''

from socket import AF_INET, SOCK_DGRAM, socket
from time import ctime

host = ''
port = 62555
addr = (host, port)

s = socket(AF_INET, SOCK_DGRAM)
s.bind(addr)
# udp无listen()

while True:
    print('waiting for massage...')
    
    data, addr = s.recvfrom(1024)
    s.sendto('[%s] %s'%(ctime(), data),addr)

    print('received data:',data)
    print('returned to:',addr)
s.close()