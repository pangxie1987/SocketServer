# #-*- coding:utf-8 -*-
# '''
# Test file
# '''

# '''
# ipaddress
# '''
# import ipaddress
# ip='123.45.67.64/27'

# net=ipaddress.ip_network(ip)
# print(net)
# for adress in net:
#     pass
#     # print(adress)

# inet=ipaddress.ip_interface(ip)
# print(inet)
# print(inet.ip)


# from socketserver import TCPServer,ThreadingTCPServer,BaseRequestHandler
# from socket import socket,AF_INET,SOCK_STREAM

# '''
# 直接用socket创建Server
# '''
# serv=socket(AF_INET,SOCK_STREAM)
# serv.bind(('127.0.0.1',8000))
# serv.listen(5)
# while True:
#     conn,addr=serv.accept()
#     print('Got connection from ',addr)
#     while True:
#         data=conn.recv(1024)
#         print(data,len(data))
#         conn.sendall(b'i am Server')
#         if len(data)==0:
#             print('close connection')
#             conn.close()
#             break
# serv.close()

'''
多线程，Event的使用
'''
# from threading import Thread,Event
# import time

# def countall(n,start_evt):
#     print('countall starting')
#     start_evt.set()
#     while n>0:
#         #print(n)
#         print('T-minus', n)
#         n-=1
#         time.sleep(2)

# start_evt=Event()
# print('Launching countall')
# t=Thread(target=countall,args=(10,start_evt))
# t.start()
# # t.join()
# start_evt.wait()
# print('countall is running')


# '''
# 获取输入或者读取文件模块fileinput
# '''
# import fileinput
# with fileinput.input('.\TestClient.py') as f:
#     for line in f:
#         print(f.filelineno(),line,end='\n')

# '''
# 提示密码输入（与平台无关）
# '''
# import getpass
# # 获取当前的用户名
# user=getpass.getuser()
# print(user)
# # 提示用户输入密码，并不显示当前的输入（pycharm无法使用）
# pswd=getpass.getpass(prompt='Password:',stream=None)
# print(pswd)

# '''
# 获取终端的大小,pychram无法使用
# '''
# import os
# size=os.get_terminal_size()
# print(size)

# '''
# 执行命令
# '''
# import subprocess
# text_bytes=subprocess.check_output(['netatat','-a'])
# print(text_bytes)

'''
webbrowser打开游览器
'''
# import webbrowser
# # 使用默认的浏览器打开
# webbrowser.open('http://www.baidu.com')

# # 获取Chrome浏览器
# wb=webbrowser.get('chrome')
# wb.open('http://www.baidu.com')