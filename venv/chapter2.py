import cv2
import numpy as np
#basic codes for openCV

img = cv2.imread("Resources/IMG_6374.JPG")
print(img.shape)
imgResized = cv2.resize(img,(0,0),fx=0.2,fy=0.2)
# kernel = np.ones((5,5),np.uint8)
#
# imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
#
# #edge detector
# imgCanny = cv2.Canny(img,2000,3000)
#
# #edge dialation (making thicker)
# imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)
#
# #edge eroded (making edge thinner)
# imgEroded = cv2.erode(imgDialation,kernel,iterations=1)
#
#
# cv2.imshow("Gray Image",imgGray)
# cv2.imshow("Blur Image",imgBlur)
# cv2.imshow("Canny Image",imgCanny)
# cv2.imshow("Diation Image",imgDialation)
# cv2.imshow("Eroded Image",imgEroded)
# cv2.waitKey(0)


# kernel = np.ones((5,5),np.uint8)

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)

#edge detector
imgCanny = cv2.Canny(imgResized,100,100)
#
# #edge dialation (making thicker)
# imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)
#
# #edge eroded (making edge thinner)
# imgEroded = cv2.erode(imgDialation,kernel,iterations=1)


cv2.imshow("ResizedImage",imgResized)
# cv2.imshow("Gray Image",imgGray)
# cv2.imshow("Blur Image",imgBlur)
cv2.imshow("Canny Image",imgCanny)
# cv2.imshow("Diation Image",imgDialation)
# cv2.imshow("Eroded Image",imgEroded)
cv2.waitKey(0)