import cv2
import numpy as np
from other import myUtlis


frameWdith = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)

while True:
    success, img = cap.read()
    cs2.imshow("Result", img)

    kernel = np.ones((5,5), np.uint8)
    print(kernel)

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray,(7,7), 0)
    imgCanny = cv2.Canny(imgBlur, 100, 200)
    imgDilation = cv2.dilate(imgCanny, kernel, iterations=2)
    imgEroded = cv2.erode(imgDilation, kernel, iterations=2)

    imgBlank = np.zeros((200,200), np.uint8)

    StackedImages = myUtlis.stackImages(0.5, ([img, imgGray, imgBlur], [imgCanny, imgDilation, imgEroded]))
    cv2.imshow("Stacked Images", StackedImages)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#https://www.youtube.com/watch?v=Wv0PSs0dmVI&list=PLMoSUbG1Q_r_sc0x7ndCsqdIkL7dwrmNF&index=6