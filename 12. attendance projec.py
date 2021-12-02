#--------1. 抽取IMAGE 轉成RGB
import cv2
import face_recognition
import os
import numpy as np
import datetime

path = "img file"                 #file that we search for
images = []                       #image list
classNames = []                    #item names
mylist = os.listdir(path)         #print the file in folder
print(mylist)
#寫一個程式可以在file 找他    們是否

for name in mylist:
    saveImg = cv2.imread(f'{path}/{name}')           #將路徑內的檔案名定義
    images.append(saveImg)                           #增加到images list (pixel)
    classNames.append(os.path.splitext(name)[0])     #增加到class names (str name)

print(classNames)

def findEncodings(images):                                   ##### 寫一個DEF 進行大量encode
    encodeList = []
    for img in images: #抽查所有file內的文件
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)           ##  先轉為RGB
        encode = face_recognition.face_encodings(img)[0]     ##  進行encode
        encodeList.append(encode)                            ##  加密後再加入表內
    return encodeList

encodeListKnown = findEncodings(images)                      ## call function to see it is ok
print(len(encodeListKnown))


def markAttendance(name):
    with open("attendance.csv", "r") as df:                  #打開CSV
        myDataList = df.readlines()
        nameList = []                                         #開表格名稱
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.datetime.now()                   #設定日期
            dtString = now.strftime('%H:%M:%S')              #設定輸入時間
            df.writelines(f'\n{name}, {dtString}')



#######################setup a cam and take the attendance
# cap =cv2.VideoCapture(0) #### cam setup
# cap = cv2.VideoCapture(path1)   #### video
# img = cv2.imread(path1)    ###  photo

path1 = "C:/Users/carro/Desktop/test3.jpg"
img = cv2.imread(path1)   #### video

while True:
    #success, img = cap.read()
    #imgS = cv2.resize(img, (0,0), None, 0.25, 0.25)        #重整大小
    imgS = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)           #將新入影像RGB化

    new_faceFrame = face_recognition.face_locations(imgS)                   #將新入影像放入face recognition
    new_encodesFrame = face_recognition.face_encodings(imgS, new_faceFrame) #將放入後進行加密

    for encodeFace, faceLoc in zip(new_encodesFrame, new_faceFrame):           #就原圖片的面部影象及加密不停loop
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)  #與FILE中的文件核對
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)  #與file中文件核對距離
        print(faceDis) #if cam opening, will frint different faceDis           #讀出與不同照片間的差值
        matchIndex = np.argmin(faceDis)                                        #讀出核對的圖片項目(最低分)

        if matches[matchIndex]:                                                #就配對中最低分的項目
            name = classNames[matchIndex].upper()                              #大草名字
            print(name)                                                        #標出

            ## if using cam, you have to multiply the size and use minus and plue to change the rectangle size
            ## y1, x2, y2, x1 = faceLoc   and times 4???
            cv2.rectangle(img, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (0,255,0), 2)          #引用loop的faceloc #畫出正方框線
            cv2.rectangle(img, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[0]), (0,255,0), cv2.FILLED)  #畫出名字的底線
            cv2.putText(img, name, (faceLoc[3], faceLoc[0]), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255),2) #寫出名字
            markAttendance(name)

    cv2.imshow('Video', img)
    cv2.waitKey(1)

