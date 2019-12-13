import numpy as np 
import cv2

#准备摄像头
cap = cv2.VideoCapture(0)  #0是调取本地摄像头

#设置每一帧宽度和高度
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))+1
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))+1

#设置视频格式
videoWriter = cv2.VideoWriter('./me.avi',cv2.VideoWriter_fourcc('P','M','4','2'),24,(w,h))

#导入素材库
detector = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')

#录入帧
while cap.isOpened():
    flag,frame = cap.read()
    if flag ==False:
        break
    gary = cv2.cvtColor(frame,code=cv2.COLOR_BGR2GRAY)
    face_zone = detector.detectMultiScale(gary,scaleFactor=1.2,minNeighbors=5)

    #人脸识别框
    for x,y,w,h in face_zone:
        cv2.rectangle(frame,pt1=(x,y),pt2=(x+w,y+h),color=[0,0,255],thickness=2)
    videoWriter.write(frame)
    if flag == False:
        break
    cv2.imshow('M',frame)

    if ord('q') == cv2.waitKey(20):
        break 
cv2.destroyAllWindows()
assert isinstance(cap.release, object)
cap.release()