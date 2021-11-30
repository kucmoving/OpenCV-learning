import cv2
import numpy as np

#---------------------------------
webCamFeed = True
pathImage = "C:/Users/carro/Desktop/1.jpg"

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)

#---------------------------
def empty(a):
    pass


def getContours(img, imgContour):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) #在圖片中找極端的POINT
    for cnt in contours:
        area = cv2.contourArea(cnt)                              #定義出contours 內每一個的面積
        areaMin = cv2.getTrackbarPos("Area", "Parameters")       #設定最少面積
        if area > areaMin:                                          #要大於最少面積才展示
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 255), 8) #進行畫圖，依照位置，畫所有圖，全部顏色，大小粗幼
            peri = cv2.arcLength(cnt, True)                      #尋找物件的邊線
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)    #尋找身件的角數, 再定義是什麼圖形
            #print(approx)                                       #得到點數位置
            #print(len(approx))                                  #得到一個OBJECT上的點數

            x, y, w, h = cv2.boundingRect(approx)                                    #設定位置
            cv2.rectangle(imgContour, (x, y), (x + w, y + h), (0, 255, 0), 5)        #設定長方形
            cv2.putText(imgContour, "Points: " + str(len(approx)), (x + w + 20, y + 20), cv2.FONT_HERSHEY_COMPLEX, .7,
                        (0, 255, 0), 2)                                              #指出文字(point)
            cv2.putText(imgContour, "Area: " + str(int(area)), (x + w + 20, y + 45), cv2.FONT_HERSHEY_COMPLEX, 0.7,
                        (0, 255, 0), 2)                                              #指出文字(area)


cv2.namedWindow("Parameters")
cv2.resizeWindow("Parameters", 640, 240)
cv2.createTrackbar("Threshold1", "Parameters", 1, 255, empty)  #---------------adjust to no too much noise
cv2.createTrackbar("Threshold2", "Parameters", 49, 255, empty) #---------------adjust to no too much noise
cv2.createTrackbar("Area", "Parameters", 5000, 30000, empty)   #---------------setup一個可以自由調整大小的trackbar

while True:
    #success, img = cap.read() if real cam
    img = cv2.imread(pathImage)   #否則用照片

    imgBlur = cv2.GaussianBlur(img, (7,7),1)                      #addblur
    imgGray = cv2.cvtColor(imgBlur, cv2.COLOR_BGR2GRAY)           #addGray

    threshold1 = cv2.getTrackbarPos("Threshold1", "Parameters")
    threshold2 = cv2.getTrackbarPos("Threshold2", "Parameters")
    imgCanny = cv2.Canny(imgGray, threshold1, threshold2)         #canny 可以看到邊界, 但前提是要BLUR 及GRAY

    kernel = np.ones((3,3))
    imgDil = cv2.dilate(imgCanny, kernel, iterations=1)            #dialte 進行擴張再清noise，kernel 是參數

    imgContor = img.copy()                                          #複製1塊IMG
    getContours(imgDil, imgContor)                                   #從原本及 imgdil 中尋找特別點


    cv2.imshow("1", img)
    cv2.imshow("2", imgGray)
    cv2.imshow("3", imgCanny)
    cv2.imshow("4", imgDil)
    cv2.imshow("5", imgContor)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break