#coding=utf-8
#放置到树莓派上

####################################电机控制库导入和初始化
from bottle import get,post,run,request,template
import RPi.GPIO as GPIO
import time
import sys 
from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor
import time
import atexit
def turnOffMotors():
	mh.getMotor(1).run(Raspi_MotorHAT.RELEASE)
	mh.getMotor(2).run(Raspi_MotorHAT.RELEASE)
	mh.getMotor(3).run(Raspi_MotorHAT.RELEASE)
	mh.getMotor(4).run(Raspi_MotorHAT.RELEASE)
mh = Raspi_MotorHAT(addr=0x40)
myMotor1 = mh.getMotor(1)
myMotor2 = mh.getMotor(2)
myMotor3 = mh.getMotor(3)
myMotor4 = mh.getMotor(4)
SPEED=150
####  定义Car类
class Car(object):
	def __init__(self):
		
		atexit.register(turnOffMotors)
		################################# DC motor test!

###############################################end######################

#######################################套接字控制初始化和库导入
from socket import *
import threading
address='127.0.0.1'     #监听哪些网络  127.0.0.1是监听本机 0.0.0.0是监听整个网络
port=12345             #监听自己的哪个端口
buffsize=1024          #接收从客户端发来的数据的缓存区大小
s = socket(AF_INET, SOCK_STREAM)
s.bind((address,port))
s.listen(2)     #最大连接数
	

#x表示移动速度，y表示车平移角度，z表示相机朝向的角度
def adjustment(x,y,z):
	SPEED=x
	car = Car()
	


def tcplink(sock,addr):
    while True:  
        recvdata=clientsock.recv(buffsize).decode('utf-8')
        if recvdata=='exit' or not recvdata:
            break
        senddata=recvdata+'from sever'
        clientsock.send(senddata.encode())
    clientsock.close()

while True:
    clientsock,clientaddress=s.accept()
    print('connect from:',clientaddress)
#传输数据都利用clientsock，和s无关
    t=threading.Thread(target=tcplink,args=(clientsock,clientaddress))  #t为新创建的线程
    t.start()
s.close()
