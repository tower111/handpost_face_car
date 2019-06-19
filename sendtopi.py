#coding=utf-8

from socket import *
#import pickle
import time


test=0
address=''
if test:
    address ='127.0.0.1'   # 监听哪些网络  127.0.0.1是监听本机 0.0.0.0是监听整个网络
else:
    address='192.168.43.139'

port=1234           #服务器的端口号
buffsize=1024     #接收数据的缓存大小
s=socket(AF_INET, SOCK_STREAM)
#s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) #重用服务端的IP和端口 (如果服务端的IP及端口在短时间内释放掉，那么就把之前的IP及端口重用上，就可以解决端口被占用问题)
s.connect((address,port))
########################################################################send data

face=open("Dlib_face_recognition_from_camera/face","r")
hand=open("HandPose/hand","r")
handpost=open("HandPose/handpost","r")


context0=""


context1_prev=""

#读取三个文件，如果读取到的数据和上次一样就不发送，不一样就发送，没0.5秒读取一次
#问题：
handlist_prev=""
count=10 #每次读取10次文件如果10次文件中有
X=2       #X次是同一个手势（Garbage）则认为识别到这个手势，识别到这个手势之后开始给小车发送人脸位置信息
x=0
while True:
    time.sleep(0.1)
    if x<X: #进行手势检测
        i=1
        while True:
            i+=1
            if i==count or x>=X:
                break

            #print("xxxxxx= ",x)

            handpost.seek(0,0)
            #handlist.append(handpost.read())
            pose=handpost.read()
            if pose=="":
                i=i-1

                continue
            #print ("i=",i)

            #print(pose)
            handlist=pose.split(',')
            #print(handlist[0],handlist[1])
            print("handlist_prev=",handlist_prev)
            if handlist_prev == handlist[0]:#如果跟前一个相等就不用再加了确保一组里面没有文件没有更新而读出内容相同
                i=i-1
                #print("aaaaaaaa",i)
                continue

            handlist_prev = handlist[0]

            if (handlist[1] == "Garbage")or (handlist[1] == "Four"):
                x+=1
        if x<X:
            x=0


    if (x >= X):
        context1=face.read()
        face.seek(0,0)
        print(context1)
        if  (context1!=""):
            print(context1)
            s.send(context1.encode())




    #i+=1

    # time.sleep(0.5)
    #
    #
    #
    #
    # a1=face.read()+'\n'
    # a2=hand.read()
    # a3=handpost.read()
    #
    #
    #
    # hand.seek(0, 0)
    # face.seek(0, 0)
    # handpost.seek(0, 0)
    #
    # # hand.truncate()
    # # hand.flush()
    # # face.truncate()
    # # face.flush()
    # # handpost.truncate()
    # # handpost.flush()
    #
    #
    #
    # if (a1=="\n") :
    #     continue
    #
    # context1= a1+a2+a3
    #
    #
    #
    # if a1_context0!=a1:
    #     print(context1)
    #     s.send(context1.encode())
    #
    # a1_context0 = a1
    # a2_context0=a2
    # a3_context0=a3
    #
    # #print(i)




