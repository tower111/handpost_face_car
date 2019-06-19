**参考**
https://github.com/MrEliptik/HandPose##TODO
**简介**
做了一些修改这里再加上我的理解。

用了多进程方式实现手势识别。多进程会让识别速度更快。（Pool）（python的多线程是在一个cpu上运行的，只有多进程才能实现多核同同时工作）。
获取参数的模式值得学习

运行`/home/tower/桌面/my_hands_fase/HandPose/HandPose.py`，先运行多进程初始化，用队列来实现进程间通信。
进程池中每个进程用来解析相机捕获到的图像，识别出手的位置并保存到队列。
然后在主进程里面输出。


**重点函数**

这里为了实现手势识别主要关注2个函数。

/home/tower/桌面/my_hands_fase/HandPose/HandPose.py
```
res = detector_utils.get_box_image(cap_params['num_hands_detect'], cap_params["score_thresh"],
                scores, boxes, cap_params['im_width'], cap_params['im_height'], frame,f)
```
这个函数在这里定义

`/home/tower/桌面/my_hands_fase/HandPose/utils/detector_utils.py`
```
#检测手的数量，是手的阀值，scores, boxes,宽，高，原始数据帧
def get_box_image(num_hands_detect, score_thresh, scores, boxes, im_width, im_height, image_np,f):

    for i in range(num_hands_detect):
        if (scores[i] > score_thresh):
            (left, right, top, bottom) = (boxes[i][1] * im_width, boxes[i][3] * im_width,
                                          boxes[i][0] * im_height, boxes[i][2] * im_height)
            print("left, right, top, bottom: ",left, right, top, bottom)


            f.write(str(left//1)+","+str(bottom//1)+","+str((bottom-top)//1)+"\n")

            #这里是手的位置
            p1 = (int(left), int(top))
            p2 = (int(right), int(bottom))


            return image_np[int(top):int(bottom), int(left):int(right)].copy()

```
这里展示了手的位置，可以找到收的坐标，这里我选择写入文件。


/home/tower/桌面/my_hands_fase/HandPose/gui.py这个文件负责输出柱型表，会在这里可以保存这是什么手势

```
def drawInferences(values, names=['', '', '', '', '', '',''],k=0):
    f = open("handpost", "w")
    nb_classes              = len(values)
    print("nb_classes",nb_classes)
    left_margin             = 150
    margin                  = 50
    thickness               = 40

    font                    = cv2.FONT_HERSHEY_SIMPLEX
    fontScale               = 1
    fontColor               = (255,255,255)
    lineType                = 2

    blank = np.zeros((350,600,3), np.uint8)

    for i in range(nb_classes):
        #决定什么时候是黄颜色
        if(values[i] > 0.4 and names[i]!='a'):
            #图像，矩阵左上点坐标，画出矩阵的长宽，颜色，宽度
            cv2.rectangle(blank, (left_margin, margin + int(margin*i)), (left_margin + int(values[i]*200), margin + thickness + int(margin*i)), (0,255,0), -1)

            print("手势是：",values[i],names[i])

            # while True:
            #     f.seek(0,i)
            #     if f.seek.read()[0]=='\n':
            #         break
            #     i += 1
            f.write(str(k)+","+names[i])
            f.flush()

        else:
            cv2.rectangle(blank, (left_margin, margin + int(margin*i)), (left_margin + int(values[i]*200), margin + thickness + int(margin*i)), (255,0,0), -1)    
        #图像，写到图片上的字，第一个字符左下角坐标，字体颜色，字体粗细，线型
        cv2.putText(blank, names[i], (0, margin + int(margin*i) + int(thickness/2)), font, fontScale, fontColor, lineType)
        cv2.putText(blank, str(values[i]), (left_margin + 200, margin + int(margin*i) + int(thickness/2)), font, fontScale, fontColor, lineType)
    f.close()
    cv2.imshow("Inferences", blank)
```



