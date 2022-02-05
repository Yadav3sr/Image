import cv2
print("Package Imported")

#importing image
# img = cv2.imread("Resources/house.png")
#
# cv2.imshow("Output",img)
# cv2.waitKey(0)

#importing video
cap = cv2.VideoCapture("Resources/timberhouse.mp4")

# while True:
#     success, img = cap.read() #success give boolean output (1 or 0)
#     cv2.imshow("Video",img)
#     if cv2.waitKey(1) & 0xFF ==ord('q'):
#         break


# capturing using webcam
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)

while True:
    success, img = cap.read()
    cv2.imshow("Video",img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break