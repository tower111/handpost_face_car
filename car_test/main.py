#!/usr/bin/env python
# -*- coding:utf-8 -*-
# coding: utf-8


SPEED=100

import sys  
reload(sys)  
sys.setdefaultencoding('ISO-8859-1')





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

 
####  ����Car��
class Car(object):
	def __init__(self):
		
		atexit.register(turnOffMotors)
		################################# DC motor test!

 
####  setup������ʼ���˿�
	def setup(self):
		# set the speed to start, from 0 (off) to 255 (max speed)
		print ("aa")
		myMotor1.run(Raspi_MotorHAT.RELEASE)#�ڶ��ֿ������еķ�����run����
		myMotor2.run(Raspi_MotorHAT.RELEASE)
		myMotor3.run(Raspi_MotorHAT.RELEASE)
		myMotor4.run(Raspi_MotorHAT.RELEASE)

 
####  fornt������С��ǰ��
	def front(self):
		self.setup()
		myMotor1.setSpeed(SPEED)
		myMotor2.setSpeed(SPEED)
		myMotor3.setSpeed(SPEED)
		myMotor4.setSpeed(SPEED)
		print ("Forward! ")
		myMotor1.run(Raspi_MotorHAT.FORWARD)#�ڶ��ֿ������еķ�����run����
		myMotor2.run(Raspi_MotorHAT.FORWARD)
		myMotor3.run(Raspi_MotorHAT.FORWARD)
		myMotor4.run(Raspi_MotorHAT.FORWARD)
 
####  left_return������ԭ����ת
	def left_return(self):
		self.setup()
		myMotor1.setSpeed(SPEED)
		myMotor2.setSpeed(SPEED)
		myMotor3.setSpeed(SPEED)
		myMotor4.setSpeed(SPEED)
		print ("Forward! ")
		myMotor1.run(Raspi_MotorHAT.FORWARD)#�ڶ��ֿ������еķ�����run����
		myMotor2.run(Raspi_MotorHAT.BACKWARD)
		myMotor3.run(Raspi_MotorHAT.FORWARD)
		myMotor4.run(Raspi_MotorHAT.BACKWARD)
 
####  right_return������С��ԭ����ת
	def right_return(self):
		self.setup()
		myMotor1.setSpeed(SPEED)
		myMotor2.setSpeed(SPEED)
		myMotor3.setSpeed(SPEED)
		myMotor4.setSpeed(SPEED)
		print ("Forward! ")
		myMotor1.run(Raspi_MotorHAT.BACKWARD)#�ڶ��ֿ������еķ�����run����
		myMotor2.run(Raspi_MotorHAT.FORWARD)
		myMotor3.run(Raspi_MotorHAT.BACKWARD)
		myMotor4.run(Raspi_MotorHAT.FORWARD)
 
####  rear������С������
	def rear(self):
		self.setup()
		myMotor1.setSpeed(SPEED)
		myMotor2.setSpeed(SPEED)
		myMotor3.setSpeed(SPEED)
		myMotor4.setSpeed(SPEED)
		print ("rare! ")
		myMotor1.run(Raspi_MotorHAT.BACKWARD)#�ڶ��ֿ������еķ�����run����
		myMotor2.run(Raspi_MotorHAT.BACKWARD)
		myMotor3.run(Raspi_MotorHAT.BACKWARD)
		myMotor4.run(Raspi_MotorHAT.BACKWARD)


####  left_shift������С����ƽ��
	def left_shift(self):
		self.setup()
		myMotor1.setSpeed(SPEED)
		myMotor2.setSpeed(SPEED)
		myMotor3.setSpeed(SPEED)
		myMotor4.setSpeed(SPEED)
		print ("rare! ")
		myMotor1.run(Raspi_MotorHAT.BACKWARD)#�ڶ��ֿ������еķ�����run����
		myMotor2.run(Raspi_MotorHAT.FORWARD)
		myMotor3.run(Raspi_MotorHAT.FORWARD)
		myMotor4.run(Raspi_MotorHAT.BACKWARD)
 
#��ƽ��
	def right_shift(self):
		self.setup()
		myMotor1.setSpeed(SPEED)
		myMotor2.setSpeed(SPEED)
		myMotor3.setSpeed(SPEED)
		myMotor4.setSpeed(SPEED)
		print ("rare! ")
		myMotor1.run(Raspi_MotorHAT.FORWARD)#�ڶ��ֿ������еķ�����run����
		myMotor2.run(Raspi_MotorHAT.BACKWARD)
		myMotor3.run(Raspi_MotorHAT.BACKWARD)
		myMotor4.run(Raspi_MotorHAT.FORWARD)
 
####  ����main������
def main(status):
	car = Car()

	if status == "front":
		car.front()
	elif status == "leftFront":
		car.left_return()
	elif status == "rightFront":
		car.right_return()
	elif status == "rear":
		car.rear()
	elif status == "leftRear":
		car.left_shift()
	elif status == "rightRear":
		car.right_shift()
	elif status == "stop":
		car.setup()      
			 
 
 
 
@get("/")
def index():
	return template("index")
@post("/cmd")
def cmd():
	adss=request.body.read().decode()
	print("press:"+adss)
	main(adss)
	return "OK"
run(host="0.0.0.0")
