#face detection using Viola and Jones method

import cv2
import numpy as np

#adding cascade
faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")

path = 'Resources/lena.png'
img = cv2.imread(path)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

faces =faceCascade.detectMultiScale(imgGray,1.1,4)

#santosh modified here

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

cv2.imshow("Result",img)
cv2.imshow("Result_Gray",imgGray)
cv2.imshow("Result_HSV",imgHSV)
cv2.waitKey(0)
cv2.destroyWindow(all())