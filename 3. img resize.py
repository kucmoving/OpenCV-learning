import cv2

path1 = "C:/Users/carro/Desktop/tomato.png"
img = cv2.imread(path1)
###print(img.shape) to check the shape of it  (h,w,RGB)


width, height = 200, 200                   # setup a resize value, no quality
img = cv2.resize(img, (width, height))     # to resize


imgCropped = img[100:150, 100:150]                                      #可以反覆切割
imgCropResized = cv2.resize(imgCropped, (img.shape[1], img.shape[0]))   #將CHOP的部份還原成原圖比例大小

cv2.imshow("Road", img)
cv2.imshow("Road", imgCropped)
cv2.imshow("Road", imgCropResized)
cv2.waitKey(0)