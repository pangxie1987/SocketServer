from socket import socket, AF_INET, SOCK_STREAM
import time
import json

# s = socket(AF_INET, SOCK_STREAM)

# s.connect(('10.253.117.127', 7900))

# print(s)

# while True:
#     # msg = (input(">>:").strip()).encode('utf-8')
#     # if len(msg) == 0:
#     #     continue
#     # elif msg == b'exit':
#     #     break
#     # s.sendall(msg)
#     # data = s.recv(1024)
#     # print('Received:', data)
#     s.sendall(b'9999')
#     time.sleep(0.5)
#     print('msg')
#     #print(s.recv(2))
# s.close()
import threading

with open ('Server/host.json') as f:
    conf = json.load(f)
    host = str(conf['host'])
    port = conf['port']
    nthreads = conf['threads']

def test():
    try:
        s = socket(AF_INET, SOCK_STREAM)

        s.connect((host, port))
        
        s.send(b'1')
    except Exception, e:
        print(e)
    else:
        print('connect sucess!')

    time.sleep(10000)

ts = []
for i in range(nthreads):
    t = threading.Thread(target=test)
    t.setDaemon(False)
    t.start()
    ts.append(t)

for t in ts:
    t.join()

