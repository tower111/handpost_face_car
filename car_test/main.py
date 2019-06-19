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

 
####  定义Car类
class Car(object):
	def __init__(self):
		
		atexit.register(turnOffMotors)
		################################# DC motor test!

 
####  setup函数初始化端口
	def setup(self):
		# set the speed to start, from 0 (off) to 255 (max speed)
		print ("aa")
		myMotor1.run(Raspi_MotorHAT.RELEASE)#第二种控制运行的方法，run函数
		myMotor2.run(Raspi_MotorHAT.RELEASE)
		myMotor3.run(Raspi_MotorHAT.RELEASE)
		myMotor4.run(Raspi_MotorHAT.RELEASE)

 
####  fornt函数，小车前进
	def front(self):
		self.setup()
		myMotor1.setSpeed(SPEED)
		myMotor2.setSpeed(SPEED)
		myMotor3.setSpeed(SPEED)
		myMotor4.setSpeed(SPEED)
		print ("Forward! ")
		myMotor1.run(Raspi_MotorHAT.FORWARD)#第二种控制运行的方法，run函数
		myMotor2.run(Raspi_MotorHAT.FORWARD)
		myMotor3.run(Raspi_MotorHAT.FORWARD)
		myMotor4.run(Raspi_MotorHAT.FORWARD)
 
####  left_return函数，原地左转
	def left_return(self):
		self.setup()
		myMotor1.setSpeed(SPEED)
		myMotor2.setSpeed(SPEED)
		myMotor3.setSpeed(SPEED)
		myMotor4.setSpeed(SPEED)
		print ("Forward! ")
		myMotor1.run(Raspi_MotorHAT.FORWARD)#第二种控制运行的方法，run函数
		myMotor2.run(Raspi_MotorHAT.BACKWARD)
		myMotor3.run(Raspi_MotorHAT.FORWARD)
		myMotor4.run(Raspi_MotorHAT.BACKWARD)
 
####  right_return函数，小车原地右转
	def right_return(self):
		self.setup()
		myMotor1.setSpeed(SPEED)
		myMotor2.setSpeed(SPEED)
		myMotor3.setSpeed(SPEED)
		myMotor4.setSpeed(SPEED)
		print ("Forward! ")
		myMotor1.run(Raspi_MotorHAT.BACKWARD)#第二种控制运行的方法，run函数
		myMotor2.run(Raspi_MotorHAT.FORWARD)
		myMotor3.run(Raspi_MotorHAT.BACKWARD)
		myMotor4.run(Raspi_MotorHAT.FORWARD)
 
####  rear函数，小车后退
	def rear(self):
		self.setup()
		myMotor1.setSpeed(SPEED)
		myMotor2.setSpeed(SPEED)
		myMotor3.setSpeed(SPEED)
		myMotor4.setSpeed(SPEED)
		print ("rare! ")
		myMotor1.run(Raspi_MotorHAT.BACKWARD)#第二种控制运行的方法，run函数
		myMotor2.run(Raspi_MotorHAT.BACKWARD)
		myMotor3.run(Raspi_MotorHAT.BACKWARD)
		myMotor4.run(Raspi_MotorHAT.BACKWARD)


####  left_shift函数，小车左平移
	def left_shift(self):
		self.setup()
		myMotor1.setSpeed(SPEED)
		myMotor2.setSpeed(SPEED)
		myMotor3.setSpeed(SPEED)
		myMotor4.setSpeed(SPEED)
		print ("rare! ")
		myMotor1.run(Raspi_MotorHAT.BACKWARD)#第二种控制运行的方法，run函数
		myMotor2.run(Raspi_MotorHAT.FORWARD)
		myMotor3.run(Raspi_MotorHAT.FORWARD)
		myMotor4.run(Raspi_MotorHAT.BACKWARD)
 
#右平移
	def right_shift(self):
		self.setup()
		myMotor1.setSpeed(SPEED)
		myMotor2.setSpeed(SPEED)
		myMotor3.setSpeed(SPEED)
		myMotor4.setSpeed(SPEED)
		print ("rare! ")
		myMotor1.run(Raspi_MotorHAT.FORWARD)#第二种控制运行的方法，run函数
		myMotor2.run(Raspi_MotorHAT.BACKWARD)
		myMotor3.run(Raspi_MotorHAT.BACKWARD)
		myMotor4.run(Raspi_MotorHAT.FORWARD)
 
####  定义main主函数
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
