import numpy as np 
import cv2

sg = cv2.imread('./aa.jpg')  #路径不能有中文
sg1 = cv2.cvtColor(sg,code=cv2.COLOR_BGR2GRAY)
#cv2.imshow('1',sg)
#cv2.waitKey(2000)   #等待键盘输入，0为无限等待  1000毫秒=1s
cv2.imshow('2',sg1)
cv2.waitKey(1000)