#coding=utf-8
import cv2


cap = cv2.VideoCapture("http://192.168.123.11:8083/?action=stream?dummy=param.mjpg")
face_cascade = cv2.CascadeClassifier(r'haarcascade_frontalface_alt.xml')  # 加载人脸特征库


############################################send_init##########################
#coding=utf-8
#客户端与上一个没有任何改变
from socket import *
import pickle


address='192.168.123.11'   #服务器的ip地址
port=1234           #服务器的端口号
buffsize=1024        #接收数据的缓存大小
s=socket(AF_INET, SOCK_STREAM)
s.connect((address,port))
########################################################################send data





while True:
    ret, frame = cap.read()
    cap.read()# 读取一帧的图像
    cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # 转灰

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.15, minNeighbors=1, minSize=(5, 5))  # 检测人脸

    save_w=[]
    for(x, y, w, h) in faces:
        save_w.append(w) #save_w将会获得一组face里面w（也就是人脸框的边长）最大的
        #cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 2)  # 用矩形圈出人脸
    if save_w:
        index_max_w=save_w.index(max(save_w))
        cv2.rectangle(frame, (faces[index_max_w][0], faces[index_max_w][1]), (faces[index_max_w][0] + max(save_w), faces[index_max_w][1] + max(save_w)), (255, 255, 255), 2)  # 用矩形圈出人脸

        if faces[index_max_w][1]<=350 and faces[index_max_w][1]>=0:
            print(faces[index_max_w])
            #if faces[index_max_w]:
            s.send(pickle.dumps(faces[index_max_w]))#将w最大的一组face发送给客户端

    cv2.imshow('Face Recognition', frame) #显示图像窗口

    if cv2.waitKey(1) & 0xFF == ord('q'):  #q键退出检测
        break

cap.release()  # 释放摄像头
cv2.destroyAllWindows()
