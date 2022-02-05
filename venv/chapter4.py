#shape and text
import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
print(img.shape)
# img[:]=100,120,10 # B,G,R value ranging from 0 to 255
# img[100:200,200:300]=100,120,10

# cv2.line(img,(0,0),(300,300),(0,255,0),3)

cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)

cv2.rectangle(img,(0,0),(250,350),(0,0,255),2)

# cv2.rectangle(img,(0,0),(250,350),(0,0,255),cv2.FILLED)

cv2.circle(img,(200,200),50,(255,120,50),2)

#putting text
cv2.putText(img,"SANTOSH",(300,200),cv2.FONT_HERSHEY_SIMPLEX,1,(0,150,0),2)

cv2.imshow("Image",img)

cv2.waitKey(0)