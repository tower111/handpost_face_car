#coding=utf-8
#放置到树莓派上
import pickle
#######################################套接字控制初始化和库导入
from socket import *
import threading


test=0
address=''
if test:
    address ='127.0.0.1'   # 监听哪些网络  127.0.0.1是监听本机 0.0.0.0是监听整个网络
else:
    address='192.168.43.139'


port=1234             #监听自己的哪个端口
buffsize=1024          #接收从客户端发来的数据的缓存区大小
s = socket(AF_INET, SOCK_STREAM)
s.bind((address,port))
s.listen(2)     #最大连接数



def tcplink(sock,addr):
    f = open("faceandhand", "w")
    while True:
        face = sock.recv(buffsize)
        if face == '':
            break

        print(face)
        print(face.decode())
        f.seek(0, 0)
        f.truncate()
        f.write(face.decode().split("\t")[0])
        f.flush()
    sock.close()
    f.close()

while True:
    clientsock,clientaddress=s.accept()
    print('connect from:',clientaddress)
    t=threading.Thread(target=tcplink,args=(clientsock,clientaddress))  #t为新创建的线程
    t.start()
s.close()
