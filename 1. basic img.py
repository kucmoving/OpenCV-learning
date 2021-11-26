import cv2

path1 = "C:/Users/carro/Desktop/tomato.png"
img = cv2.imread(path1)
print(img)
# img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) to be grey
# img = cv2.GaussianBlur(img,(7,7),0)        to be blur
# img = cv2.Canny(imgBlur,100,100) to show the edge only

# import numpy as np                                # import np
# kernel = np.ones((5,5), np.uint8)                 # setup size of matrix
# img = cv2.dilate(img, kernel, iterations = 3)     # 進行擴張
# img = cv2.erode(img, kernel, iterations = 3)       #進行收窄侵蝕

cv2.imshow("tomato", img) # to give a name
cv2.waitKey(0) # the time to hold