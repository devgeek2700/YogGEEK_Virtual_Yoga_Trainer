import cv2
import mediapipe as mp
import time
import math
import numpy as np


class PoseDetector:
    def __init__(self, mode=False, maxHands=1, modelComplexity=1, upBody=False, smooth=True, detectionCon=0.5,
                 trackCon=0.5):

        self.mode = mode
        self.maxHands = maxHands
        self.modelComplex = modelComplexity
        self.upBody = upBody
        self.smooth = smooth
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.mode, self.maxHands, self.modelComplex, self.upBody, self.smooth,
                                     self.detectionCon, self.trackCon)

#detection of pose

    def findPose(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        # print(results.pose_landmarks)
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)

        return img

    def getPosition(self, img, draw=True):
        self.lmList = []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                print(id, lm)
                cx, cy = int(lm.x * w), int(lm.y * h)
                self.lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
        return self.lmList

    def findAngle(self, img, p1, p2, p3,p4,p5, draw=True):
     

        # finding the landmarks

        x1, y1 = self.lmList[p1][1:]
        x2, y2 = self.lmList[p2][1:]
        x3, y3 = self.lmList[p3][1:]
        x4, y4 = self.lmList[p4][1:]
        x5, y5 = self.lmList[p5][1:]
        




        # calculating the angle between those main landmarks like (x2, y2)
        angle = math.degrees(math.atan2(y3 - y2, x3 - x2) -
                             math.atan2(y1 - y2, x1 - x2))
        
         # to avoid negative angles:-

        # if angle < 0:
        #     angle += 360

       
        print(angle)
       

        if draw:
            #draw line to detect the main points for detection


            #circle key points for angle calcuation:-
            cv2.circle(img, (x1, y1), 10, (242, 34, 240), cv2.FILLED)
            cv2.circle(img, (x1, y1), 10, (242, 34, 240), cv2.FILLED)
            cv2.circle(img, (x1, y1), 5, (242, 34, 240), cv2.FILLED)
            cv2.circle(img, (x1, y1), 10, (242, 34, 240), 2)
            cv2.circle(img, (x2, y2), 5, (242, 34, 240), cv2.FILLED)
            cv2.circle(img, (x2, y2), 10, (242, 34, 240), 2)
            cv2.circle(img, (x3, y3), 5, (242, 34, 240), cv2.FILLED)
            cv2.circle(img, (x3, y3), 10, (242, 34, 240), 2)
            cv2.circle(img, (x4, y4), 5, (242, 34, 240), cv2.FILLED)
            cv2.circle(img, (x4, y4), 10, (242, 34, 240), 2)
            cv2.circle(img, (x5, y5), 5, (242, 34, 240), cv2.FILLED)
            cv2.circle(img, (x5, y5), 10, (242, 34, 240), 2)
            cv2.putText(img, str(int(angle)), (x2 - 50, y2 + 50),
                        cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
        return angle


def main():
    cap = cv2.VideoCapture(0)
    pTime = 0
    detector = PoseDetector()
    while True:
        success, img = cap.read()
        img = detector.findPose(img)
        lmList = detector.getPosition(img)
        print(lmList)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 3)
        cv2.imshow("Image", img)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()