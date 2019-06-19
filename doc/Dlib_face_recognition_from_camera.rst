**参考**

https://github.com/coneypo/Dlib_face_recognition_from_camera

原本程序提供了添加人脸具体使用参考上面链接。


**简介**

程序检测到人脸提取人脸的主要信息，跟数据库进行对比，如果相似度高就认为是这个人。


主程序/home/tower/桌面/my_hands_fase/Dlib_face_recognition_from_camera/face_reco_from_camera_bat.py

为了需要我添加了读文件的代码，不停handpost读文件，读出来的数据先检测索引判断数据是否发生过改变。

然后判断是否和上一次相等

count=5 #每次读取10次文件如果10次文件中有
X=3       #X次是同一个手势（Garbage）则认为识别到这个手势，识别到这个手势之后开始给小车发送人脸位置信息
满足5次里面读到的有三次符合的手势才会执行后面的操作，检测要么是识别不够准要么是识别到手的可能太难，效果不是太好，几个重要参数都给出了注释。


```
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
        K=0
        address = ''
        if test:
            address = '127.0.0.1'  # 监听哪些网络  127.0.0.1是监听本机 0.0.0.0是监听整个网络
        else:
            address = '192.168.43.139'
        port = 1234  # 服务器的端口号
        buffsize = 1024  # 接收数据的缓存大小
        s = socket(AF_INET, SOCK_STREAM)
        s.connect((address, port))

```




这里记录了一个被检测到人的人脸位置信息，我添加了发送的代码
```
 if min(e_distance_list) < 0.5:#判断欧氏距离，找到

                            # 在这里修改 person_1, person_2 ... 的名字
                            # 可以在这里改称 Jack, Tom and others
                            # Here you can modify the names shown on the camera
                            name_namelist[k] = "Person "+str(int(similar_person_num)+1)

                            # 找到一个已经记录的人脸,显示底部，顶部，高度信息
                            print("left: " + str(faces[k].left()) + "    bottom: " + str(faces[k].bottom()) + "  weigh: " + str(
                                (faces[k].bottom() - faces[k].top()) / 4))

                            s.send((str(faces[k].left()) + "," + str(faces[k].bottom()) + "," +
                                    str(int(faces[k].bottom() - faces[k].top())) + ",person" + str(int(similar_person_num)+1) + "\t").encode())
                            # f.write(str(faces[k].left()) + "," + str(faces[k].bottom()) + "," +
                            #         str(int(faces[k].bottom() - faces[k].top())) + ",person" + str(int(similar_person_num)+1) + "\t")
                            #
                            # f.flush()

```
