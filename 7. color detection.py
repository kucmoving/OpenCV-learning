import cv2
import numpy as np

path = "C:/Users/carro/Desktop/tomato.png"

def empty(a):  #設定空白function,a 是parameters
    pass

# have to setup 3value with max and min
cv2.namedWindow("TrackBars")# build up track bar win
cv2.resizeWindow("TrackBars", 640, 240)
cv2.createTrackbar("Hue Min", "TrackBars", 5, 179, empty) #name, in which window, min, max, function call
cv2.createTrackbar("Hue Max", "TrackBars", 179, 179, empty)
cv2.createTrackbar("Sat Min", "TrackBars", 0, 255, empty) #name, in which window, min, max, function call
cv2.createTrackbar("Sat Max", "TrackBars", 181, 255, empty)
cv2.createTrackbar("Val Min", "TrackBars", 162, 255, empty) #name, in which window, min, max, function call
cv2.createTrackbar("Val Max", "TrackBars", 255, 255, empty)


while True:
    img = cv2.imread(path)
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #change it to be ImgHSV
    # #define color value(saturation) (value limit: max, min)
    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars") # variable = window and trackbar item
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars") # variable = window and trackbar item
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars") # variable = window and trackbar item
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars") # variable = window and trackbar item
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars") # variable = window and trackbar item
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars") # variable = window and trackbar item

    # setup lower , upper in mask  / put imgHSV in mask
    print(h_min, h_max, s_min, s_max, v_min, v_max)  # use this to filter out particular color
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    mask = cv2.inRange(imgHSV, lower, upper)
    # to check the color you want(調整中最後留有白色，再數值改成6個項目的第一個數字)
    imgResult = cv2.bitwise_and(img, img, mask=mask) #to link the origin and the mask, to be a new pic(get the color)

    cv2.imshow("Original", img)
    cv2.imshow("HSV", imgHSV)
    cv2.imshow("Mask", mask)
    cv2.imshow("Result", imgResult)
    cv2.waitKey(1)                               #1是關閉, 配while loop 不停刷新