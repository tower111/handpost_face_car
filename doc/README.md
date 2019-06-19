**服务器上**

**搭建环境**

```
安装virtualenv
➜  ~ pip install virtualenv
找到python安装路径
➜  ~ whereis python3
python3: /usr/bin/python3.5 /usr/bin/python3.5m /usr/bin/python3 /usr/bin/python3.5m-config /usr/bin/python3.5-config /usr/lib/python3.5 /usr/lib/python3 /etc/python3.5 /etc/python3 /usr/local/lib/python3.5 /usr/include/python3.5 /usr/include/python3.5m /usr/share/python3 /home/tower/anaconda3/bin/python3.6m-config /home/tower/anaconda3/bin/python3.6m /home/tower/anaconda3/bin/python3.6-config /home/tower/anaconda3/bin/python3 /home/tower/anaconda3/bin/python3.6 /usr/share/man/man1/python3.1.gz

创建虚拟环境
➜  ~ virtualenv -p /usr/bin/python3.5  cv3

进入环境
➜  ~ workon cv3
安装库（需要什么库装什么就可以了）：
pip install 库名字


```




**`face_reco_from_camera_bat.py`**

face_reco_from_camera.py是修改的多线程的但是修改失败了

文件里面不光有人脸识别还加入了python套接字发送给树莓派的代码，原版访问https://github.com/coneypo/Dlib_face_recognition_from_camera

树莓派需要先运行`./car_test/recv_from_server.py`

先读取handPost文件读取出来手势的 用来人脸识别，得到人脸的位置（左下角坐标和画出方框的高度）还有这个人是谁

运行：`python3 ./Dlib_face_recognition_from_camera/face_reco_from_camera.py` 


**`HandPost.py`**

用来实现手势识别，得到手的位置（左下角坐标和画出方框的高度）还有这个手势是什么手势文件分别保存到`hand`，`handpost`
``

运行：`python3 ./HandPose/HandPose.py`


****
**树莓派上**


http://10.139.14.2:8083/

树莓派端工作目录：/home/pi/Documents/car_test/

**0x01运行相机**

环境搭建https://blog.csdn.net/qq_35614920/article/details/77113467

把相机发送到一个端口上
```
cd ~/mjpg-streamer-master/mjpg-streamer-experimental
./mjpg_streamer -i "./input_uvc.so" -o "./output_http.so -p 8083 -w ./www"
```

**0x02  recv_from_server.py**

接收到的是一组字符串里面格式如下

```
282,426,26.75,person2    #人脸的左下角坐标，人脸矩阵的高度，人名    检测到多个人脸会保存已经被录入人脸中最大的

```
并把字符串保存到`andpost`

**0x03 control.py**

从handandpost文件里面读取脸和手的信息通过这些信息控制小车移动。
****

**优缺点分析，需要改进的问题**

**0x01**

使用文件来进行通信速度较慢，效率比较低。可以改进为进程池控制进程，队列通信。

手势识别不是太精准。人脸识别延迟太高。


**0x02延迟问题**

对延迟问题的优化主要就是减少处理的帧数，

****
**参考**

人脸识别部分 https://github.com/coneypo/Dlib_face_recognition_from_camera

手势识别部分 https://github.com/MrEliptik/HandPose##TODO
****

**运行**



**树莓派上**

cd ~/mjpg-streamer-master/mjpg-streamer-experimental  && ./mjpg_streamer -i "./input_uvc.so" -o "./output_http.so -p 8083 -w ./www"   运行相机   把相机视频数据发送到web上。

cd ~/Documents/car_test && python  recv_from_server.py  接收信息

cd ~/Documents/car_test && python  control.py   控制移动

**服务器端**

workon cv && cd./HandPose && python HandPose.py        检测人手（会写入文件一个序号和手势，这个序号可以确定一段时间内手势是否刷新）

workon cv && cd Dlib_face_recognition_from_camera && python face_reco_from_camera_bat.py  检测人脸（首先读取handPost文件，检测到读取到的数据中是否有需要的手势，如果有，检测人脸，并和数据库比较如果已经录入就发送给树莓派）
****
**其他**



`face_check.py`是一个检测人脸的并发送的简单脚本，只能实现检测到人脸，并不能检测这个人是谁。 没有保存人脸特征。不过优点也很明显就是速度快，延迟低这里用的是opencv haar

Dlib_face_recognition_from_camera用的是dlib cnn优缺点参考链接 https://www.52pojie.cn/thread-819328-1-1.html

具体应用起来基本上能满足需求但是优化的空间很大。







