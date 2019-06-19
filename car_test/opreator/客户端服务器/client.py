
#coding=utf-8
#客户端与上一个没有任何改变
from socket import *
address='127.0.0.1'   #服务器的ip地址
port=12345           #服务器的端口号
buffsize=1024        #接收数据的缓存大小
s=socket(AF_INET, SOCK_STREAM)
s.connect((address,port))
while True:
    senddata=raw_input('想要发送的数据：')
    if senddata=='exit':
        break
    s.send(senddata.encode())
    recvdata=s.recv(buffsize).decode('utf-8')
    print(recvdata)
s.close()

