import cv2

frameWidth = 640    ##
frameHeight = 360    ### it must fit the cam size if u using cam
#cap = cv2.VideoCapture(0) #setup the cam...
#cap.set(3, frameWidth)
#cap.set(4, frameHeight)

cap = cv2.VideoCapture("C:/Users/carro/Desktop/123.mp4")

while True:
    success, img = cap.read()                       #to show the cap
    img = cv2.resize(img, (frameWidth, frameHeight)) #to resize
    cv2.imshow('123',img)                            #to add the file name

    if cv2.waitKey(1) & 0xFF == ord('q'):    #按"Q"會離開BREAK(注意大細階)    #1會展示畫面
        break
