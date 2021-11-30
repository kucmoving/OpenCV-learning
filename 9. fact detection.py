import cv2

faceCascade = cv2.CascadeClassifier("C:/Users/carro/Desktop/haarcascade_frontalface_default.xml")
#####can download different xml , this is too old but works

img = cv2.imread('C:/Users/carro/Desktop/family.jpg')
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)

cv2.imshow('family', img)
cv2.waitKey(0)
#opencv has a lot of cascades ==> to classify eye, eye glass.....
