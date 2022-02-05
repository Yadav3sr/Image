#cropping and resizing image
import cv2
import numpy as np

img = cv2.imread("Resources/house.png")
print(img.shape)

imgResize = cv2.resize(img,(400,800))  # (width, height)
print(imgResize.shape)

#cropping an image
imgCropped = img[0:200,200:500]  #(height, width)

cv2.imshow("Image",img)
# cv2.imshow("Image Resize",imgResize)
cv2.imshow("Cropped Image",imgCropped)

cv2.waitKey(0)