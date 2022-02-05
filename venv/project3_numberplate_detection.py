import cv2
import numpy as np

#adding cascade
numberPlateCascade = cv2.CascadeClassifier("Resources/haarcascade_russian_plate_number.xml")
minArea = 500
color = (255,0,0)
count = 0
##################
path = 'Resources/car.png'
img = cv2.imread(path)
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

numberPlate =numberPlateCascade.detectMultiScale(imgGray,1.1,4)

for (x,y,w,h) in numberPlate:
    area = w*h
    if area > minArea:
        cv2.rectangle(img,(x,y),(x+w,y+h),color,2)
        cv2.putText(img,"Number Plate",(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,1,color,2)
        imgRoi = img[y:y+h,x:x+w]
        cv2.imshow("ROI",imgRoi)


cv2.imshow("Result",img)
if cv2.waitKey(0) & 0xFF == ord('s'):
    cv2.imwrite("Resources/Scanned/Noplate_"+str(count)+".jpg",imgRoi)
    cv2.rectange(img,(0,200),(640,300),(0,255,0),cv2.FILLED)
    cv2.putText(img,"Scan saved",(150,265),cv2.FONT_HERSHEY_SIMPLEX,2,color,2)
    count +=1
    cv2.imshow("Result",img)
    cv2.waitKey(500)
# cv2.destroyWindow(all())