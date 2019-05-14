# -*- coding: utf-8 -*-

import cv2
import numpy as np


def recall_nothing():
    pass


# 创建一幅三通道的图
image = np.zeros((200, 300,3), dtype=np.float64)
cv2.namedWindow('Image')

# 创建滑动条
cv2.createTrackbar('a', 'Image', 0, 300, recall_nothing)
cv2.createTrackbar('b', 'Image', 0, 300, recall_nothing)
cv2.createTrackbar('m1', 'Image', 0, 300, recall_nothing)
cv2.createTrackbar('w1', 'Image', 0, 100, recall_nothing)
cv2.createTrackbar('m2', 'Image', 0, 300, recall_nothing)
cv2.createTrackbar('w2', 'Image', 0, 100, recall_nothing)






# 创建开关(0表示关闭RGB的调色效果，此时效果为黑)
#switch = '0:OFF\n1:ON'
#cv2.createTrackbar(switch, 'Image', 0, 1, recall_nothing)


while 1:
    cv2.imshow('Image', image)
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        # 'ESC键代表退出'
        break
    # 获得各个滑动条的值
    a = cv2.getTrackbarPos('a', 'Image')
    b = cv2.getTrackbarPos('b', 'Image')
    m1 = cv2.getTrackbarPos('m1', 'Image')
    w1 = cv2.getTrackbarPos('w1', 'Image')
    m2 = cv2.getTrackbarPos('m2', 'Image')
    w2 = cv2.getTrackbarPos('w2', 'Image')



   # w1= cv2.getTrackbarPos(switch, 'Image')
    
    # 显示
   # if s == 0:
        # 开关关闭，显示全黑
       # image[:] = 0
   # else:
        # 对于彩色图像(RGB),OpenCV按照BGR来显示，Matplotlib按照RGB来显示
    image[:] = [b,b,b]

