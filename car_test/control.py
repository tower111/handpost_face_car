#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding: utf-8


SPEED = 80

import sys

# reload(sys)
# sys.setdefaultencoding('ISO-8859-1')

from bottle import get, post, run, request, template

import RPi.GPIO as GPIO
import time
import sys

from Raspi_MotorHAT import Raspi_MotorHAT, Raspi_DCMotor
import time
import atexit

############定义移动的单位（休眠时间）
U_FR = 0.2  # 定义前后平移的单位
U_RLS = 0.2  # 定义左右平移单位
U_XS = 1  # 定义斜向平移单位
U_RLT = 0.05  # 左右旋转单位

##############允许误差+-
E_PX = 25  # x和y的允许误差
E_PW = 5  # w的允许误差
X = 254  # 理想化的x
Y = 83  # 理想化的Y
W = 50  # 理想化的W


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

import mmap
import contextlib
import time
import pickle

s1 = "1234"


def get_face():
    m = open('faceandhand', 'r')
    while True:
        global s1
        s = m.read()
        # print("s",s)
        if not (',' in s) or s1 in s:
            m.seek(0,0)
            time.sleep(0.1)
            continue
        print(s)
        s = s.split("\t")[0]

        face = s.split(",")
        print(face)
        print(len(face))
        for i in range(len(face) - 1):
            face[i] = int(face[i])
        print(face)

        if ((face[0]>=X-E_PX)and(face[0]<=X+E_PX))and((face[2]>=W-E_PW) and (face[2]<=W+E_PW)):
            continue

        s1 = s
        m.close()
        break

    return face


# def get_context():
#     while True:
#         global s1
#         m = open('test.dat', 'r')
#         s = m.read()
#         if not (',' in s) or s == s1:#如果，不在(说明原文件为空) s==s1说明文件没有更该没必要移动
#             time.sleep(0.01)#一直没有新的输入会“阻塞”到这里
#             continue
#         print(s)
#         context = s.split("\n")
#         face = context[0].split(",")
#         hand = (context[1] + context[2]).split(",")
#         for i in range(len(context)-1):
#             face[i]=int(face[i],10)
#             hand[i]=int(hand[i],10)
#
#         print(face)
#         print(hand)
#         s1 = s
#         break
#     return face,hand

####  ����Car��
class Car(object):
    def __init__(self):
        atexit.register(turnOffMotors)

    ################################# DC motor test!

    ####  setup������ʼ���˿�
    def setup(self):
        # set the speed to start, from 0 (off) to 255 (max speed)
        print("aa")
        myMotor1.run(Raspi_MotorHAT.RELEASE)  # �ڶ��ֿ������еķ�����run����
        myMotor2.run(Raspi_MotorHAT.RELEASE)
        myMotor3.run(Raspi_MotorHAT.RELEASE)
        myMotor4.run(Raspi_MotorHAT.RELEASE)

    ####  left_turn函数，原地左转
    def left_turn(self):
        self.setup()
        myMotor1.setSpeed(SPEED)
        myMotor2.setSpeed(SPEED)
        myMotor3.setSpeed(SPEED)
        myMotor4.setSpeed(SPEED)
        print("left_turn")
        myMotor1.run(Raspi_MotorHAT.FORWARD)  # 第二种控制运行的方法，run函数
        myMotor2.run(Raspi_MotorHAT.BACKWARD)
        myMotor3.run(Raspi_MotorHAT.FORWARD)
        myMotor4.run(Raspi_MotorHAT.BACKWARD)
        time.sleep(U_RLT)
        self.setup()

    ####  right_turn函数，小车原地右转
    def right_turn(self):
        self.setup()
        myMotor1.setSpeed(SPEED)
        myMotor2.setSpeed(SPEED)
        myMotor3.setSpeed(SPEED)
        myMotor4.setSpeed(SPEED)
        print("right_turn! ")
        myMotor1.run(Raspi_MotorHAT.BACKWARD)  # 第二种控制运行的方法，run函数
        myMotor2.run(Raspi_MotorHAT.FORWARD)
        myMotor3.run(Raspi_MotorHAT.BACKWARD)
        myMotor4.run(Raspi_MotorHAT.FORWARD)
        time.sleep(U_RLT)
        self.setup()
        # 前进

    def front(self):
        self.setup()
        myMotor1.setSpeed(SPEED)
        myMotor2.setSpeed(SPEED)
        myMotor3.setSpeed(SPEED)
        myMotor4.setSpeed(SPEED)
        print("front! ")
        myMotor1.run(Raspi_MotorHAT.FORWARD)  # 第二种控制运行的方法，run函数
        myMotor2.run(Raspi_MotorHAT.FORWARD)
        myMotor3.run(Raspi_MotorHAT.FORWARD)
        myMotor4.run(Raspi_MotorHAT.FORWARD)
        time.sleep(U_FR)
        self.setup()

    ####  rear函数，小车后退
    def rear(self):
        self.setup()
        myMotor1.setSpeed(SPEED)
        myMotor2.setSpeed(SPEED)
        myMotor3.setSpeed(SPEED)
        myMotor4.setSpeed(SPEED)
        print("rare! ")
        myMotor1.run(Raspi_MotorHAT.BACKWARD)  # 第二种控制运行的方法，run函数
        myMotor2.run(Raspi_MotorHAT.BACKWARD)
        myMotor3.run(Raspi_MotorHAT.BACKWARD)
        myMotor4.run(Raspi_MotorHAT.BACKWARD)
        time.sleep(U_FR)
        self.setup()

    # 右前平移
    def right_front_shift(self):
        self.setup()
        myMotor1.setSpeed(SPEED)
        myMotor2.setSpeed(0)
        myMotor3.setSpeed(0)
        myMotor4.setSpeed(SPEED)
        print("right_front_shift! ")
        myMotor1.run(Raspi_MotorHAT.FORWARD)  # 第二种控制运行的方法，run函数
        myMotor2.run(Raspi_MotorHAT.BACKWARD)
        myMotor3.run(Raspi_MotorHAT.FORWARD)
        myMotor4.run(Raspi_MotorHAT.FORWARD)
        time.sleep(U_XS)
        self.setup()

    ####  left_shift函数，小车左后平移
    def left_rear_shift(self):
        self.setup()
        myMotor1.setSpeed(SPEED)
        myMotor2.setSpeed(0)
        myMotor3.setSpeed(0)
        myMotor4.setSpeed(SPEED)
        print("left_rear_shift! ")
        myMotor1.run(Raspi_MotorHAT.BACKWARD)  # 第二种控制运行的方法，run函数
        myMotor2.run(Raspi_MotorHAT.BACKWARD)
        myMotor3.run(Raspi_MotorHAT.FORWARD)
        myMotor4.run(Raspi_MotorHAT.BACKWARD)
        time.sleep(U_XS)
        self.setup()

    # 左前方
    def left_front_shift(self):
        self.setup()
        myMotor1.setSpeed(0)
        myMotor2.setSpeed(SPEED)
        myMotor3.setSpeed(SPEED)
        myMotor4.setSpeed(0)
        print("left_front_shift! ")
        myMotor1.run(Raspi_MotorHAT.FORWARD)  # 第二种控制运行的方法，run函数
        myMotor2.run(Raspi_MotorHAT.FORWARD)
        myMotor3.run(Raspi_MotorHAT.FORWARD)
        myMotor4.run(Raspi_MotorHAT.FORWARD)
        time.sleep(U_XS)
        self.setup()

    # 右后方
    def right_rear_shift(self):
        self.setup()
        myMotor1.setSpeed(0)
        myMotor2.setSpeed(SPEED)
        myMotor3.setSpeed(SPEED)
        myMotor4.setSpeed(0)
        print("right_rear_shift! ")
        myMotor1.run(Raspi_MotorHAT.FORWARD)  # 第二种控制运行的方法，run函数
        myMotor2.run(Raspi_MotorHAT.BACKWARD)
        myMotor3.run(Raspi_MotorHAT.BACKWARD)
        myMotor4.run(Raspi_MotorHAT.FORWARD)
        time.sleep(U_XS)
        self.setup()

    # 右平移
    def right_shift(self):
        self.setup()
        myMotor1.setSpeed(SPEED)
        myMotor2.setSpeed(SPEED)
        myMotor3.setSpeed(SPEED)
        myMotor4.setSpeed(SPEED)
        print("right_shift! ")
        myMotor1.run(Raspi_MotorHAT.FORWARD)  # 第二种控制运行的方法，run函数
        myMotor2.run(Raspi_MotorHAT.BACKWARD)
        myMotor3.run(Raspi_MotorHAT.BACKWARD)
        myMotor4.run(Raspi_MotorHAT.FORWARD)
        time.sleep(U_RLS)
        self.setup()

    # 左平移
    def left_shift(self):
        self.setup()
        myMotor1.setSpeed(SPEED)
        myMotor2.setSpeed(SPEED)
        myMotor3.setSpeed(SPEED)
        myMotor4.setSpeed(SPEED)
        print("left_shift! ")
        myMotor1.run(Raspi_MotorHAT.BACKWARD)  # 第二种控制运行的方法，run函数
        myMotor2.run(Raspi_MotorHAT.FORWARD)
        myMotor3.run(Raspi_MotorHAT.FORWARD)
        myMotor4.run(Raspi_MotorHAT.BACKWARD)
        time.sleep(U_RLS)
        self.setup()


def RotationMode(car):  # 以自转方式找到对应位置
    face = get_face()  # 获取到参数
    while (face[0] >= X + E_PX) or face[0] <= X - E_PX:
        # if (face[2] >= W + E_PW) or (face[2] <= W - E_PW):
        #     break
        if face[0] >= X + E_PX:
            car.right_turn()
        elif face[0] <= X - E_PX:
            car.left_turn()
        face = get_face()  # 刷新参数


def RFMode(car):  # 以平移方式移动
    face = get_face()  # 获取到参数
    while (face[0] >= X + E_PX) or face[0] <= X - E_PX:

        if face[0] >= X + E_PX:
            car.right_shift()
        elif face[0] <= X - E_PX:
            car.left_shift()
        face = get_face()  # 刷新参数


# def tiaozheng(car):#如果识别到人脸是已经录入的就自转以调整位置
#     face, hand = get_context()  # 获取到参数
#
#     while (face[0] >= X + E_PX) or face[0] <= X - E_PX:
#         if (face[3] != "unknow"):
#             if face[0] >= X + E_PX:
#                 car.right_shift()
#             elif face[0] <= X - E_PX:
#                 car.left_shift()
#         else:
#             time.sleep(0.2)
#         face, hand = get_context()  # 刷新参数


####  ����main������
def main():
    car = Car()
    while True:
        # RotationMode(car)
        RotationMode(car)
        face = get_face()  # 获取到参数
        while (face[2] >= W + E_PW) or face[2] <= W - E_PW:
            # if (face[0] >= X + E_PX) or (face[0] <= X - E_PX):  # 打断前后运行
            #     break
            if face[2] >= W + E_PW:
                car.rear()
            elif face[2] <= W - E_PW:
                car.front()
            face = get_face()  # 刷新参数 # 获取到参数
        time.sleep(1)

        # 拍照


main()
#
#
#     if status == "front":
#         car.front()
#     elif status == "leftFront":
#         car.left_return()
#     elif status == "rightFront":
#         car.right_return()
#     elif status == "rear":
#         car.rear()
#     elif status == "leftRear":
#         car.left_shift()
#     elif status == "rightRear":
#         car.right_shift()
#     elif status == "stop":
#         car.setup()
#
#
# @get("/")
# def index():
#     return template("index")
#
#
# @post("/cmd")
# def cmd():
#     adss = request.body.read().decode()
#     print("press:" + adss)
#     main(adss)
#     return "OK"
#
#
# run(host="0.0.0.0")
