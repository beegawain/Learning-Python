import numpy as np 
import cv2

xz = cv2.imread('./xz.jpg')
#人脸数据、级联分类器，给人脸特征数据，返回可以识别人脸的对象
detector = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
face_zone = detector.detectMultiScale(xz)

for x,y,w,h in face_zone:
    cv2.rectangle(xz,pt1=(x,y),pt2=(x+w,y+h),color=[0,0,255])
cv2.imshow('xz',xz)
cv2.waitKey(0)
cv2.destroyAllWindows()