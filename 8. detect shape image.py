import cv2
import numpy as np

def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) #用findcontours, 尋找圖形大細
    for cnt in contours:
        area = cv2.contourArea(cnt)                                                       #取得每個圖形的大少
        print(area)
        if area > 500:                                                                    #設定畫圖門檻
            cv2.drawContours(imgContour, cnt, -1, (255, 0, 0),3) #進行劃圖, 於imgcontour之上,畫每個cnt, 所有圖形,顏色,粗幼
            peri = cv2.arcLength(cnt, True)                      #計算每個邊界的長度，TRUE 代表一個一個計
            #print(peri)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)      #計算有幾多個corner, 0.02 是可以調整, true是因為close 圖形)
            print(len(approx))

            x, y, w, h = cv2.boundingRect(approx)                             #畫出框框
            cv2.rectangle(imgContour, (x,y), (x+w, y+h), (0, 255, 0),2)       #畫出為一個長方形,顏色,粗幼

            objCor = (len(approx))                                            #圖像識別﹕物體外點數量
            if objCor ==3:                                                    #設定ohject分類條件
                objectType = "Tri"
            elif objCor ==4:
                aspRatio = w/float(h)
                if aspRatio > 0.95 and aspRatio < 1.05:
                    objectType = "Square"
                else:
                    objectType = "Rectangle"
            elif objCor>4:
                objectType= "Circles"
            else:
                objectType = "None"
                                                                              #標示出相關文字
            cv2.putText(imgContour, objectType,
                        (x+(w//2)-10, y+(h//2)-10), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,150,0), 1)




path = 'C:/Users/carro/Desktop/picture.jpg'
img = cv2.imread(path)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)      #-------------進行灰階
imgBlur = cv2.GaussianBlur(imgGray, (7,7), 1)        #-------------進行BLUR
imgCanny = cv2.Canny(imgBlur, 50, 50)                #-------------模糊化
imgBlank = np.zeros_like(img)
imgContour = img.copy()

getContours(imgCanny)

cv2.imshow("Original", img)
cv2.imshow("Gray", imgGray)
cv2.imshow("Blur", imgBlur)
cv2.imshow("Canny", imgCanny)
cv2.imshow("Blank", imgBlank)
cv2.imshow("Contour", imgContour)

cv2.waitKey(0)