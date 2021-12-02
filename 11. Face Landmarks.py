import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture("C:/Users/carro/Desktop/456.mp4")

pTime = 0

mpDraw = mp.solutions.drawing_utils                                                     #畫出點點
mpFaceMesh = mp.solutions.face_mesh                                                     #套用網狀
faceMesh = mpFaceMesh.FaceMesh(max_num_faces=3)                                       #進行追縱、數目 CTRL+R 睇有咩參數
drawSpec = mpDraw.DrawingSpec(thickness=1, circle_radius=1)                            #to set the thickness and radius

while True:
    success, img = cap.read()                                                               #show the cam

    cTime = time.time()
    fps = 1 /(cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)})', (20,70), cv2.FONT_HERSHEY_PLAIN,
                3, (0,255,0), 3) #location, font, scale, color, width


    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)                                        #轉入RGB予facemesh執行
    results = faceMesh.process(imgRGB)                                                   #進行套用
    if results.multi_face_landmarks:
        for faceLms in results.multi_face_landmarks:
            mpDraw.draw_landmarks(img, faceLms, mpFaceMesh.FACEMESH_TESSELATION          #attribute changed
                                  ,drawSpec, drawSpec)
            for id, lm in enumerate(faceLms.landmark):            #抓出每張圖的網格座點, id是 1-486粒 , lm 是每格h,w,c
                ####print(lm)
                ih, iw, ic = img.shape                  #height, width, channel --> pixel
                x, y = int(lm.x*iw), int(lm.y*ih)
                print(id,x,y)                              #印出座標


    cv2.imshow("Image", img)
    cv2.waitKey(1)