import cv2
import mediapipe as mp
import time


class FaceMeshDetector():

    def __init__(self, static_image_mode=False, max_num_faces=2, refine_landmarks=False, min_detection_confidence=0.5,
                 min_tracking_confidence=0.5):                     #setup default attribute(parameters)
        self.static_image_mode = static_image_mode                 #add self (variable created in this class)
        self.max_num_faces = max_num_faces
        self.refine_landmarks = refine_landmarks
        self.min_detection_confidence = min_detection_confidence
        self.min_tracking_confidence = min_tracking_confidence

        self.mpDraw = mp.solutions.drawing_utils                                                     #畫出點點
        self.mpFaceMesh = mp.solutions.face_mesh                                                     #套用網狀
        self.faceMesh = self.mpFaceMesh.FaceMesh(self.static_image_mode, self.max_num_faces,
                                                 self.refine_landmarks,
                                            self.min_detection_confidence, self.min_tracking_confidence)#進行追縱、數目 CTRL+R 睇有咩參數
        self.drawSpec = self.mpDraw.DrawingSpec(color=(0,255,0),thickness=1, circle_radius=1)                              #to set the thickness and radius


    def findFaceMesh(self, img, draw=True):
        self.imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)                                        #轉入RGB予facemesh執行
        self.results = self.faceMesh.process(self.imgRGB)  #進行套用
        faces = []
        if self.results.multi_face_landmarks:
            for faceLms in self.results.multi_face_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, faceLms, self.mpFaceMesh.FACEMESH_TESSELATION          #attribute changed
                                  ,self.drawSpec, self.drawSpec)
                face = []
                for id, lm in enumerate(faceLms.landmark):            #抓出每張圖的網格座點, id是 1-486粒 , lm 是每格h,w,c
                    #print(lm)
                    ih, iw, ic = img.shape                  #height, width, channel --> pixel
                    x, y = int(lm.x*iw), int(lm.y*ih)
                    #cv2.putText(img, str(id), (x,y), cv2.FONT_HERSHEY_PLAIN, 1, (0,255,0),1)
                    #print(id,x,y)                              #印出座標
                    face.append([x,y])
                faces.append(face)
        return img,faces



#設置功能main，展示鏡頭，show fps
def main():
    cap = cv2.VideoCapture("C:/Users/carro/Desktop/456.mp4")
    pTime = 0
    detector = FaceMeshDetector()
    while True:
        success, img = cap.read()  # show the cam
        img, faces = detector.findFaceMesh(img)
        if len(faces) != 0:
            print(faces[0])
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, f'FPS: {int(fps)})', (20,70), cv2.FONT_HERSHEY_PLAIN,
                3, (0,255,0), 3) #location, font, scale, color, width
        cv2.imshow("Image", img)
        cv2.waitKey(1)

if __name__ == "__main__":
    main()