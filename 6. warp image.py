import cv2
import numpy as np

path1 = "C:/Users/carro/Desktop/poker2.jpg"
img = cv2.imread(path1)

width, height = 100, 150
pts1 = np.array([[83,37], [163,21], [108,164], [189,149]], np.float32) #turn on paint and search the x,y
pts2 = np.array([[0,0], [width,0], [0,height], [width,height]], np.float32)
print(pts1)

matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))


cv2.imshow('poker2', img)
cv2.imshow('poker2', imgOutput)
cv2.waitKey(0)

