####  left_turn函数，原地左转
def left_turn(self):
	self.setup()
	myMotor1.setSpeed(SPEED)
	myMotor2.setSpeed(SPEED)
	myMotor3.setSpeed(SPEED)
	myMotor4.setSpeed(SPEED)
	print("Forward! ")
	myMotor1.run(Raspi_MotorHAT.FORWARD)  # 第二种控制运行的方法，run函数
	myMotor2.run(Raspi_MotorHAT.BACKWARD)
	myMotor3.run(Raspi_MotorHAT.FORWARD)
	myMotor4.run(Raspi_MotorHAT.BACKWARD)


####  right_turn函数，小车原地右转
def right_turn(self):
	self.setup()
	myMotor1.setSpeed(SPEED)
	myMotor2.setSpeed(SPEED)
	myMotor3.setSpeed(SPEED)
	myMotor4.setSpeed(SPEED)
	print("Forward! ")
	myMotor1.run(Raspi_MotorHAT.BACKWARD)  # 第二种控制运行的方法，run函数
	myMotor2.run(Raspi_MotorHAT.FORWARD)
	myMotor3.run(Raspi_MotorHAT.BACKWARD)
	myMotor4.run(Raspi_MotorHAT.FORWARD)
#前进
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


#右前平移
	def right_front_shift(self):
		self.setup()
		myMotor1.setSpeed(SPEED)
		myMotor2.setSpeed(0)
		myMotor3.setSpeed(0)
		myMotor4.setSpeed(SPEED)
		print ("rare! ")
		myMotor1.run(Raspi_MotorHAT.FORWARD)#第二种控制运行的方法，run函数
		myMotor2.run(Raspi_MotorHAT.BACKWARD)
		myMotor3.run(Raspi_MotorHAT.FORWARD)
		myMotor4.run(Raspi_MotorHAT.FORWARD)

####  left_shift函数，小车左后平移
	def left_rear_shift(self):
		self.setup()
		myMotor1.setSpeed(SPEED)
		myMotor2.setSpeed(0)
		myMotor3.setSpeed(0)
		myMotor4.setSpeed(SPEED)
		print ("rare! ")
		myMotor1.run(Raspi_MotorHAT.BACKWARD)#第二种控制运行的方法，run函数
		myMotor2.run(Raspi_MotorHAT.BACKWARD)
		myMotor3.run(Raspi_MotorHAT.FORWARD)
		myMotor4.run(Raspi_MotorHAT.BACKWARD)


#左前方
	def left_front_shift(self):
		self.setup()
		myMotor1.setSpeed(0)
		myMotor2.setSpeed(SPEED)
		myMotor3.setSpeed(SPEED)
		myMotor4.setSpeed(0)
		print ("rare! ")
		myMotor1.run(Raspi_MotorHAT.FORWARD)#第二种控制运行的方法，run函数
		myMotor2.run(Raspi_MotorHAT.FORWARD)
		myMotor3.run(Raspi_MotorHAT.FORWARD)
		myMotor4.run(Raspi_MotorHAT.FORWARD)

#右后方
	def right_rear_shift(self):
		self.setup()
		myMotor1.setSpeed(0)
		myMotor2.setSpeed(SPEED)
		myMotor3.setSpeed(SPEED)
		myMotor4.setSpeed(0)
		print ("rare! ")
		myMotor1.run(Raspi_MotorHAT.FORWARD)#第二种控制运行的方法，run函数
		myMotor2.run(Raspi_MotorHAT.BACKWARD)
		myMotor3.run(Raspi_MotorHAT.BACKWARD)
		myMotor4.run(Raspi_MotorHAT.FORWARD)

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
#左平移
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
 



