
ssh pi@192.168.43.139
cd /home/pi/Documents/car_test


cd HandPose/ &&python HandPose.py
#echo ********************手势识别启动********************


pi@raspberrypi:~/Documents/car_test $ python recv_from_server.py      树莓派接收
#echo ***********************************recv*****************



pi@raspberrypi:~/Documents/car_test $ python control.py      启动控制

cd Dlib_face_recognition_from_camera/ &&python face_reco_from_camera_bat.py

print(" *******************人脸检测已经运行*****************************************")







