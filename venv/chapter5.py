import cv2
import numpy as np

img = cv2.imread("Resources/cards.png")

width,height = 250,350
#creating warp prospectives
pts1 = np.float32([[471,48],[768,36],[779,488],[487,500]])
pts2 = np.float32([[0,0],[width,0],[width,height],[0,height]])

matrix = cv2.getPerspectiveTransform(pts1,pts2)

imgOutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow("Image",img)
cv2.imshow("Output",imgOutput)
cv2.waitKey(0)