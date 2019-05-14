# -*- coding: utf-8 -*-

import cv2
import numpy as np


def recall_nothing():
    pass


# 创建一幅三通道的图
image = np.zeros((300, 500, 3), dtype=np.uint8)
cv2.namedWindow('Image')

# 创建滑动条
cv2.createTrackbar('R', 'Image', 0, 255, recall_nothing)
cv2.createTrackbar('G', 'Image', 0, 255, recall_nothing)
cv2.createTrackbar('B', 'Image', 0, 255, recall_nothing)

# 创建开关(0表示关闭RGB的调色效果，此时效果为黑)
switch = '0:OFF\n1:ON'
cv2.createTrackbar(switch, 'Image', 0, 1, recall_nothing)


while 1:
    cv2.imshow('Image', image)
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        # 'ESC键代表退出'
        break
    # 获得各个滑动条的值
    r = cv2.getTrackbarPos('R', 'Image')
    g = cv2.getTrackbarPos('G', 'Image')
    b = cv2.getTrackbarPos('B', 'Image')
    s = cv2.getTrackbarPos(switch, 'Image')

    # 显示
    if s == 0:
        # 开关关闭，显示全黑
        image[:] = 0
    else:
        # 对于彩色图像(RGB),OpenCV按照BGR来显示，Matplotlib按照RGB来显示
        image[:] = [b, g, r]
