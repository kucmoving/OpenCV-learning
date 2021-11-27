import cv2
import numpy as np

img = np.zeros((512,512,3) ,np.uint8) #np.會展示matrix  #uint8 是將matrix的數字變成int
print(img)

#img[20:30, 60:100] = 255, 78, 42  #進行部份地方上色                         #img範圍, rgb 色彩
#cv2.line(img, (0,0), (100,100), (0,255,0), 2)                            #圖片,起始線，終點線，顏色，粗幼
#cv2.line(img, (0,0), (img.shape[1], img.shape[0]), (0,255,0), 2)         #亦可以直接畫到最尾方位
#cv2.rectangle(img, (350,100), (450,200), (0,0,255), 2)                   #圖片,起始線，終點線，顏色，粗幼
#cv2.rectangle(img, (350,100), (450,200), (0,0,255), cv2.FILLED)          #cv2.FILLED進行上色
#cv2.circle(img, (150,400), 50,(255,0,0), 3)                              #50是半徑
#cv2.putText(img, "Draw Shapes", (75,50), cv2.FONT_HERSHEY_COMPLEX, 1,(0,150,0), 1) #出現的位置, 字型, SKIN, 顏色,粗幼

cv2.imshow("image", img)
cv2.waitKey(0)
