from flask import Flask,render_template,Response,redirect, url_for, request, flash, session
from unittest import result
import numpy as np
import cv2
import time 
# import tensorflow as tf
# import tensorflow_hub as hub
# from matplotlib import pyplot as plt
# import data as data
import Posemodule1 as pm
# import pythoncom
from time import sleep
# import schedule
import time
# import matplotlib.pyplot as plt 
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, UserMixin, logout_user




app = Flask(__name__)


#database for login/register

# app.config['SQLALCHEMY_TRACK_MODIFIACTIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///YogGEEK.db'
db = SQLAlchemy(app)
app.config['SECRET_KEY'] = 'thisismysecretkeyyoga'
app.app_context().push()


cap=cv2.VideoCapture(0)
detector = pm.PoseDetector()

#normal webcam

# def generate_frames():
#     while True:
            
#         ## read the camera frame
#         success,frame=cap.read()
#         if not success:
#             break
#         else:
#             ret,buffer=cv2.imencode('.jpg',frame)
#             frame=buffer.tobytes()

#         # if cv2.waitKey(1) & 0xFF == ord('q'):
#         #   break

#         yield(b'--frame\r\n'
#                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


#normal webcam with only angles

# def generate_frames():
#     while True:
#         #read the camera frames
#         success, frame = cap.read()
#         if not success:
#             break

#         #display the frames in buffer bytes in webpage
#         else:
#            img = cv2.resize(frame, (1280, 728))
#            img = detector.findPose(frame)

#            #this copying img content in frame to display
#            frame = img.copy()
#            lmlist = detector.getPosition(frame, False)
#            print(lmlist)
#            if len(lmlist) != 0:
#                # right arm
#             detector.findAngle(frame, 12, 14, 16, 18, 20)
            
#               # left arm
#             detector.findAngle(frame,11, 13, 15, 17, 19)
#               # left leg
#             detector.findAngle(frame, 23, 25, 27, 29, 31)
#               # right leg
#             detector.findAngle(frame, 24, 26, 28,30, 32)

           
           
#            ret, buffer =  cv2.imencode('.jpg', frame)
#            frame = buffer.tobytes()

#            yield(b'--frame\r\n'
#                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')



#normal webcam with acc & angles :- Palm tree pose

def palm_generate_frames():
    while True:
        #read the camera frames
        success, frame = cap.read()
        if not success:
            break

        #display the frames in buffer bytes in webpage
        else:
           img = cv2.resize(frame, (1280, 728))
           img = detector.findPose(frame)

           #this copying img content in frame to display
           frame = img.copy()
           lmlist = detector.getPosition(frame, False)
        #    print(lmlist)
           if len(lmlist) != 0:
               # right arm
            angle = detector.findAngle(frame, 12, 14, 16, 18, 20)
            per = np.interp(angle, (-155, -170), (0,100))
            if (per >= 50):
                if(per <= 100):
                    #user's left side
                    cv2.putText(frame, "Left arm accurate 65%", (15, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

            elif(per < 50):
                cv2.putText(frame, "Left arm less than 65% accurate", (15, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

            
              # left arm
            angle = detector.findAngle(frame,11, 13, 15, 17, 19)
            per = np.interp(angle, (-190, -205), (0, 100))
            if (per >= 50):
                if(per <= 100):
                    #user's right side
                    cv2.putText(frame, "Right arm accurate 65%", (350, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
            
            elif(per < 50):
                cv2.putText(frame, "Right arm less than 65% accurate", (350, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)



              # left leg
            angle = detector.findAngle(frame, 23, 25, 27, 29, 31)
            per = np.interp(angle, (175, 190), (0, 100))
            if (per >= 50):
                if(per <= 100):
                    #user's left side
                    cv2.putText(frame, "Right leg accurate 65%", (350, 450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

            elif(per < 50):
                cv2.putText(frame, "Right leg less than 65% accurate", (350, 450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)



              # right leg
            angle = detector.findAngle(frame, 24, 26, 28,30, 32)
            per = np.interp(angle, (170, 185), (0, 100))
            if (per >= 50):
                if(per <= 100):
                    #user's right side
                    cv2.putText(frame, "Left leg accurate 65%", (15, 450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

            elif(per < 50):
                cv2.putText(frame, "Left leg less than 65% accurate", (15, 450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

           
           
           ret, buffer =  cv2.imencode('.jpg', frame)
           frame = buffer.tobytes()

           yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
           

def tree_generate_frames():
    while True:
        #read the camera frames
        success, frame = cap.read()
        if not success:
            break

        #display the frames in buffer bytes in webpage
        else:
           img = cv2.resize(frame, (1280, 728))
           img = detector.findPose(frame)

           #this copying img content in frame to display
           frame = img.copy()
           lmlist = detector.getPosition(frame, False)
        #    print(lmlist)
           if len(lmlist) != 0:
               # right arm
            angle = detector.findAngle(frame, 12, 14, 16, 18, 20)
            per = np.interp(angle, ( -170,-150), (0,100))
            if (per >= 50):
                if(per <= 100):
                    #user's left side
                    cv2.putText(frame, "Left arm accurate 65%", (15, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

            elif(per < 50):
                cv2.putText(frame, "Left arm less than 65% accurate", (15, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

            
              # left arm
            angle = detector.findAngle(frame,11, 13, 15, 17, 19)
            per = np.interp(angle, (-230, -190), (0, 100))
            if (per >= 50):
                if(per <= 100):
                    #user's right side
                    cv2.putText(frame, "Right arm accurate 65%", (350, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
            
            elif(per < 50):
                cv2.putText(frame, "Right arm less than 65% accurate", (350, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)



              # left leg
            angle = detector.findAngle(frame, 23, 25, 27, 29, 31)
            per = np.interp(angle, (160, 190), (0, 100))
            if (per >= 50):
                if(per <= 100):
                    #user's left side
                    cv2.putText(frame, "Right leg accurate 65%", (350, 450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

            elif(per < 50):
                cv2.putText(frame, "Right leg less than 65% accurate", (350, 450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)



              # right leg
            angle = detector.findAngle(frame, 24, 26, 28,30, 32)
            per = np.interp(angle, (315, 325), (0, 100))
            if (per >= 50):
                if(per <= 100):
                    #user's right side
                    cv2.putText(frame, "Left leg accurate 65%", (15, 450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

            elif(per < 50):
                cv2.putText(frame, "Left leg less than 65% accurate", (15, 450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

           
           
           ret, buffer =  cv2.imencode('.jpg', frame)
           frame = buffer.tobytes()

           yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
           

def triangle_generate_frames():
    while True:
        #read the camera frames
        success, frame = cap.read()
        if not success:
            break

        #display the frames in buffer bytes in webpage
        else:
           img = cv2.resize(frame, (1280, 728))
           img = detector.findPose(frame)

           #this copying img content in frame to display
           frame = img.copy()
           lmlist = detector.getPosition(frame, False)
        #    print(lmlist)
           if len(lmlist) != 0:
               # right arm
            angle = detector.findAngle(frame, 12, 14, 16, 18, 20)
            per = np.interp(angle, (-145, -160), (0,100))
            if (per >= 50):
                if(per <= 100):
                    #user's left side
                    cv2.putText(frame, "Left arm accurate 65%", (15, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

            elif(per < 50):
                cv2.putText(frame, "Left arm less than 65% accurate", (15, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

            
              # left arm
            angle = detector.findAngle(frame,11, 13, 15, 17, 19)
            per = np.interp(angle, (20, 35), (0, 100))
            if (per >= 50):
                if(per <= 100):
                    #user's right side
                    cv2.putText(frame, "Right arm accurate 65%", (350, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
            
            elif(per < 50):
                cv2.putText(frame, "Right arm less than 65% accurate", (350, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)



              # left leg
            angle = detector.findAngle(frame, 23, 25, 27, 29, 31)
            per = np.interp(angle, (175, 190), (0, 100))
            if (per >= 50):
                if(per <= 100):
                    #user's left side
                    cv2.putText(frame, "Right leg accurate 65%", (350, 450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

            elif(per < 50):
                cv2.putText(frame, "Right leg less than 65% accurate", (350, 450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)



              # right leg
            angle = detector.findAngle(frame, 24, 26, 28,30, 32)
            per = np.interp(angle, (165, 180), (0, 100))
            if (per >= 50):
                if(per <= 100):
                    #user's right side
                    cv2.putText(frame, "Left leg accurate 65%", (15, 450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

            elif(per < 50):
                cv2.putText(frame, "Left leg less than 65% accurate", (15, 450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

           
           
           ret, buffer =  cv2.imencode('.jpg', frame)
           frame = buffer.tobytes()

           yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
           
def warrior_generate_frames():
    while True:
        #read the camera frames
        success, frame = cap.read()
        if not success:
            break

        #display the frames in buffer bytes in webpage
        else:
           img = cv2.resize(frame, (1280, 728))
           img = detector.findPose(frame)

           #this copying img content in frame to display
           frame = img.copy()
           lmlist = detector.getPosition(frame, False)
        #    print(lmlist)
           if len(lmlist) != 0:
               # right arm
            angle = detector.findAngle(frame, 12, 14, 16, 18, 20)
            per = np.interp(angle, (-185, -200), (0,100))
            if (per >= 50):
                if(per <= 100):
                    #user's left side
                    cv2.putText(frame, "Left arm accurate 65%", (15, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

            elif(per < 50):
                cv2.putText(frame, "Left arm less than 65% accurate", (15, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

            
              # left arm
            angle = detector.findAngle(frame,11, 13, 15, 17, 19)
            per = np.interp(angle, (-180, -195), (0, 100))
            if (per >= 50):
                if(per <= 100):
                    #user's right side
                    cv2.putText(frame, "Right arm accurate 65%", (350, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
            
            elif(per < 50):
                cv2.putText(frame, "Right arm less than 65% accurate", (350, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)



              # left leg
            angle = detector.findAngle(frame, 23, 25, 27, 29, 31)
            per = np.interp(angle, (185, 200), (0, 100))
            if (per >= 50):
                if(per <= 100):
                    #user's left side
                    cv2.putText(frame, "Right leg accurate 65%", (350, 450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

            elif(per < 50):
                cv2.putText(frame, "Right leg less than 65% accurate", (350, 450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)



              # right leg
            angle = detector.findAngle(frame, 24, 26, 28,30, 32)
            per = np.interp(angle, (250, 280), (0, 100))
            if (per >= 50):
                if(per <= 100):
                    #user's right side
                    cv2.putText(frame, "Left leg accurate 65%", (15, 450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

            elif(per < 50):
                cv2.putText(frame, "Left leg less than 65% accurate", (15, 450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

           
           
           ret, buffer =  cv2.imencode('.jpg', frame)
           frame = buffer.tobytes()

           yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
           
def dog_generate_frames():
    while True:
        #read the camera frames
        success, frame = cap.read()
        if not success:
            break

        #display the frames in buffer bytes in webpage
        else:
           img = cv2.resize(frame, (1280, 728))
           img = detector.findPose(frame)

           #this copying img content in frame to display
           frame = img.copy()
           lmlist = detector.getPosition(frame, False)
        #    print(lmlist)
           if len(lmlist) != 0:
               # right arm
            angle = detector.findAngle(frame, 12, 14, 16, 18, 20)
            per = np.interp(angle, (170, 190), (0,100))
            if (per >= 50):
                if(per <= 100):
                    #user's left side
                    cv2.putText(frame, "Left arm accurate 65%", (15, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

            elif(per < 50):
                cv2.putText(frame, "Left arm less than 65% accurate", (15, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

            
              # left arm
            angle = detector.findAngle(frame,11, 13, 15, 17, 19)
            per = np.interp(angle, (170, 190), (0, 100))
            if (per >= 50):
                if(per <= 100):
                    #user's right side
                    cv2.putText(frame, "Right arm accurate 65%", (350, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
            
            elif(per < 50):
                cv2.putText(frame, "Right arm less than 65% accurate", (350, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)



              # left leg
            angle = detector.findAngle(frame, 23, 25, 27, 29, 31)
            per = np.interp(angle, (170, 185), (0, 100))
            if (per >= 50):
                if(per <= 100):
                    #user's left side
                    cv2.putText(frame, "Right leg accurate 65%", (350, 450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

            elif(per < 50):
                cv2.putText(frame, "Right leg less than 65% accurate", (350, 450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)



              # right leg
            angle = detector.findAngle(frame, 24, 26, 28,30, 32)
            per = np.interp(angle, (165, 180), (0, 100))
            if (per >= 50):
                if(per <= 100):
                    #user's right side
                    cv2.putText(frame, "Left leg accurate 65%", (15, 450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

            elif(per < 50):
                cv2.putText(frame, "Left leg less than 65% accurate", (15, 450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

           
           
           ret, buffer =  cv2.imencode('.jpg', frame)
           frame = buffer.tobytes()

           yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
           
def mount_generate_frames():
    while True:
        #read the camera frames
        success, frame = cap.read()
        if not success:
            break

        #display the frames in buffer bytes in webpage
        else:
           img = cv2.resize(frame, (1280, 728))
           img = detector.findPose(frame)

           #this copying img content in frame to display
           frame = img.copy()
           lmlist = detector.getPosition(frame, False)
        #    print(lmlist)
           if len(lmlist) != 0:
               # right arm
            angle = detector.findAngle(frame, 12, 14, 16, 18, 20)
            per = np.interp(angle, (185, 200), (0,100))
            if (per >= 50):
                if(per <= 100):
                    #user's left side
                    cv2.putText(frame, "Left arm accurate 65%", (15, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

            elif(per < 50):
                cv2.putText(frame, "Left arm less than 65% accurate", (15, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

            
              # left arm
            angle = detector.findAngle(frame,11, 13, 15, 17, 19)
            per = np.interp(angle, (160, 175), (0, 100))
            if (per >= 50):
                if(per <= 100):
                    #user's right side
                    cv2.putText(frame, "Right arm accurate 65%", (350, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
            
            elif(per < 50):
                cv2.putText(frame, "Right arm less than 65% accurate", (350, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)



              # left leg
            angle = detector.findAngle(frame, 23, 25, 27, 29, 31)
            per = np.interp(angle, (170, 185), (0, 100))
            if (per >= 50):
                if(per <= 100):
                    #user's left side
                    cv2.putText(frame, "Right leg accurate 65%", (350, 450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

            elif(per < 50):
                cv2.putText(frame, "Right leg less than 65% accurate", (350, 450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)



              # right leg
            angle = detector.findAngle(frame, 24, 26, 28,30, 32)
            per = np.interp(angle, (170, 185), (0, 100))
            if (per >= 50):
                if(per <= 100):
                    #user's right side
                    cv2.putText(frame, "Left leg accurate 65%", (15, 450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

            elif(per < 50):
                cv2.putText(frame, "Left leg less than 65% accurate", (15, 450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

           
           
           ret, buffer =  cv2.imencode('.jpg', frame)
           frame = buffer.tobytes()

           yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
           

def cat_generate_frames():
    while True:
        #read the camera frames
        success, frame = cap.read()
        if not success:
            break

        #display the frames in buffer bytes in webpage
        else:
           img = cv2.resize(frame, (1280, 728))
           img = detector.findPose(frame)

           #this copying img content in frame to display
           frame = img.copy()
           lmlist = detector.getPosition(frame, False)
        #    print(lmlist)
           if len(lmlist) != 0:
               # right arm
            angle = detector.findAngle(frame, 12, 14, 16, 18, 20)
            per = np.interp(angle, (-245, -260), (0,100))
            if (per >= 50):
                if(per <= 100):
                    #user's left side
                    cv2.putText(frame, "Left arm accurate 65%", (15, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

            elif(per < 50):
                cv2.putText(frame, "Left arm less than 65% accurate", (15, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

            
              # left arm
            angle = detector.findAngle(frame,11, 13, 15, 17, 19)
            per = np.interp(angle, (-100, -110), (0, 100))
            if (per >= 50):
                if(per <= 100):
                    #user's right side
                    cv2.putText(frame, "Right arm accurate 65%", (350, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
            
            elif(per < 50):
                cv2.putText(frame, "Right arm less than 65% accurate", (350, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)



              # left leg
            angle = detector.findAngle(frame, 23, 25, 27, 29, 31)
            per = np.interp(angle, (50, 95), (0, 100))
            if (per >= 50):
                if(per <= 100):
                    #user's left side
                    cv2.putText(frame, "Right leg accurate 65%", (350, 450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

            elif(per < 50):
                cv2.putText(frame, "Right leg less than 65% accurate", (350, 450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)



              # right leg
            angle = detector.findAngle(frame, 24, 26, 28,30, 32)
            per = np.interp(angle, (50, 95), (0, 100))
            if (per >= 50):
                if(per <= 100):
                    #user's right side
                    cv2.putText(frame, "Left leg accurate 65%", (15, 450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

            elif(per < 50):
                cv2.putText(frame, "Left leg less than 65% accurate", (15, 450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

           
           
           ret, buffer =  cv2.imencode('.jpg', frame)
           frame = buffer.tobytes()

           yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
           

def camel_generate_frames():
    while True:
        #read the camera frames
        success, frame = cap.read()
        if not success:
            break

        #display the frames in buffer bytes in webpage
        else:
           img = cv2.resize(frame, (1280, 728))
           img = detector.findPose(frame)

           #this copying img content in frame to display
           frame = img.copy()
           lmlist = detector.getPosition(frame, False)
        #    print(lmlist)
           if len(lmlist) != 0:
               # right arm
            angle = detector.findAngle(frame, 12, 14, 16, 18, 20)
            per = np.interp(angle, (150, 165), (0,100))
            if (per >= 50):
                if(per <= 100):
                    #user's left side
                    cv2.putText(frame, "Left arm accurate 65%", (15, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

            elif(per < 50):
                cv2.putText(frame, "Left arm less than 65% accurate", (15, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

            
              # left arm
            angle = detector.findAngle(frame,11, 13, 15, 17, 19)
            per = np.interp(angle, (150, 165), (0, 100))
            if (per >= 50):
                if(per <= 100):
                    #user's right side
                    cv2.putText(frame, "Right arm accurate 65%", (350, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
            
            elif(per < 50):
                cv2.putText(frame, "Right arm less than 65% accurate", (350, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)



              # left leg
            angle = detector.findAngle(frame, 23, 25, 27, 29, 31)
            per = np.interp(angle, (80, 100), (0, 100))
            if (per >= 50):
                if(per <= 100):
                    #user's left side
                    cv2.putText(frame, "Right leg accurate 65%", (350, 450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

            elif(per < 50):
                cv2.putText(frame, "Right leg less than 65% accurate", (350, 450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)



              # right leg
            angle = detector.findAngle(frame, 24, 26, 28,30, 32)
            per = np.interp(angle, (80, 100), (0, 100))
            if (per >= 50):
                if(per <= 100):
                    #user's right side
                    cv2.putText(frame, "Left leg accurate 65%", (15, 450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

            elif(per < 50):
                cv2.putText(frame, "Left leg less than 65% accurate", (15, 450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

           
           
           ret, buffer =  cv2.imencode('.jpg', frame)
           frame = buffer.tobytes()

           yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
           

def sphinx_generate_frames():
    while True:
        #read the camera frames
        success, frame = cap.read()
        if not success:
            break

        #display the frames in buffer bytes in webpage
        else:
           img = cv2.resize(frame, (1280, 728))
           img = detector.findPose(frame)

           #this copying img content in frame to display
           frame = img.copy()
           lmlist = detector.getPosition(frame, False)
        #    print(lmlist)
           if len(lmlist) != 0:
               # right arm
            angle = detector.findAngle(frame, 12, 14, 16, 18, 20)
            per = np.interp(angle, (115, 130), (0,100))
            if (per >= 50):
                if(per <= 100):
                    #user's left side
                    cv2.putText(frame, "Left arm accurate 65%", (15, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

            elif(per < 50):
                cv2.putText(frame, "Left arm less than 65% accurate", (15, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

            
              # left arm
            angle = detector.findAngle(frame,11, 13, 15, 17, 19)
            per = np.interp(angle, (100, 115), (0, 100))
            if (per >= 50):
                if(per <= 100):
                    #user's right side
                    cv2.putText(frame, "Right arm accurate 65%", (350, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
            
            elif(per < 50):
                cv2.putText(frame, "Right arm less than 65% accurate", (350, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)



              # left leg
            angle = detector.findAngle(frame, 23, 25, 27, 29, 31)
            per = np.interp(angle, (-165, -180), (0, 100))
            if (per >= 50):
                if(per <= 100):
                    #user's left side
                    cv2.putText(frame, "Right leg accurate 65%", (350, 450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

            elif(per < 50):
                cv2.putText(frame, "Right leg less than 65% accurate", (350, 450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)



              # right leg
            angle = detector.findAngle(frame, 24, 26, 28,30, 32)
            per = np.interp(angle, (-165, -180), (0, 100))
            if (per >= 50):
                if(per <= 100):
                    #user's right side
                    cv2.putText(frame, "Left leg accurate 65%", (15, 450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

            elif(per < 50):
                cv2.putText(frame, "Left leg less than 65% accurate", (15, 450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

           
           
           ret, buffer =  cv2.imencode('.jpg', frame)
           frame = buffer.tobytes()

           yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
           
#change
def corpse_generate_frames():
    while True:
        #read the camera frames
        success, frame = cap.read()
        if not success:
            break

        #display the frames in buffer bytes in webpage
        else:
           img = cv2.resize(frame, (1280, 728))
           img = detector.findPose(frame)

           #this copying img content in frame to display
           frame = img.copy()
           lmlist = detector.getPosition(frame, False)
        #    print(lmlist)
           if len(lmlist) != 0:
               # right arm
            angle = detector.findAngle(frame, 12, 14, 16, 18, 20)
            per = np.interp(angle, (180, 200), (0,100))
            if (per >= 50):
                if(per <= 100):
                    #user's left side
                    cv2.putText(frame, "Left arm accurate 65%", (15, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

            elif(per < 50):
                cv2.putText(frame, "Left arm less than 65% accurate", (15, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

            
              # left arm
            angle = detector.findAngle(frame,11, 13, 15, 17, 19)
            per = np.interp(angle, (185, 200), (0, 100))
            if (per >= 50):
                if(per <= 100):
                    #user's right side
                    cv2.putText(frame, "Right arm accurate 65%", (350, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
            
            elif(per < 50):
                cv2.putText(frame, "Right arm less than 65% accurate", (350, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)



              # left leg
            angle = detector.findAngle(frame, 23, 25, 27, 29, 31)
            per = np.interp(angle, (165, 180), (0, 100))
            if (per >= 50):
                if(per <= 100):
                    #user's left side
                    cv2.putText(frame, "Right leg accurate 65%", (350, 450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

            elif(per < 50):
                cv2.putText(frame, "Right leg less than 65% accurate", (350, 450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)



              # right leg
            angle = detector.findAngle(frame, 24, 26, 28,30, 32)
            per = np.interp(angle, (155, 170), (0, 100))
            if (per >= 50):
                if(per <= 100):
                    #user's right side
                    cv2.putText(frame, "Left leg accurate 65%", (15, 450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

            elif(per < 50):
                cv2.putText(frame, "Left leg less than 65% accurate", (15, 450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

           
           
           ret, buffer =  cv2.imencode('.jpg', frame)
           frame = buffer.tobytes()

           yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
           

def goddess_generate_frames():
    while True:
        #read the camera frames
        success, frame = cap.read()
        if not success:
            break

        #display the frames in buffer bytes in webpage
        else:
           img = cv2.resize(frame, (1280, 728))
           img = detector.findPose(frame)

           #this copying img content in frame to display
           frame = img.copy()
           lmlist = detector.getPosition(frame, False)
        #    print(lmlist)
           if len(lmlist) != 0:
               # right arm
            angle = detector.findAngle(frame, 12, 14, 16, 18, 20)
            per = np.interp(angle, (-190, -110), (0,100))
            if (per >= 50):
                if(per <= 100):
                    #user's left side
                    cv2.putText(frame, "Left arm accurate 65%", (15, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

            elif(per < 50):
                cv2.putText(frame, "Left arm less than 65% accurate", (15, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

            
              # left arm
            angle = detector.findAngle(frame,11, 13, 15, 17, 19)
            per = np.interp(angle, (-250 , -265), (0, 100))
            if (per >= 50):
                if(per <= 100):
                    #user's right side
                    cv2.putText(frame, "Right arm accurate 65%", (350, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
            
            elif(per < 50):
                cv2.putText(frame, "Right arm less than 65% accurate", (350, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)



              # left leg
            angle = detector.findAngle(frame, 23, 25, 27, 29, 31)
            per = np.interp(angle, (195, 120), (0, 100))
            if (per >= 50):
                if(per <= 100):
                    #user's left side
                    cv2.putText(frame, "Right leg accurate 65%", (350, 450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

            elif(per < 50):
                cv2.putText(frame, "Right leg less than 65% accurate", (350, 450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)



              # right leg
            angle = detector.findAngle(frame, 24, 26, 28,30, 32)
            per = np.interp(angle, (240, 255), (0, 100))
            if (per >= 50):
                if(per <= 100):
                    #user's right side
                    cv2.putText(frame, "Left leg accurate 65%", (15, 450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

            elif(per < 50):
                cv2.putText(frame, "Left leg less than 65% accurate", (15, 450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

           
           
           ret, buffer =  cv2.imencode('.jpg', frame)
           frame = buffer.tobytes()

           yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
           
#perfect
def cobras_generate_frames():
    while True:
        #read the camera frames
        success, frame = cap.read()
        if not success:
            break

        #display the frames in buffer bytes in webpage
        else:
           img = cv2.resize(frame, (1280, 728))
           img = detector.findPose(frame)

           #this copying img content in frame to display
           frame = img.copy()
           lmlist = detector.getPosition(frame, False)
        #    print(lmlist)
           if len(lmlist) != 0:
               # right arm
            angle = detector.findAngle(frame, 12, 14, 16, 18, 20)
            per = np.interp(angle, (185, 200), (0,100))
            if (per >= 50):
                if(per <= 100):
                    #user's left side
                    cv2.putText(frame, "Left arm accurate 65%", (15, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

            elif(per < 50):
                cv2.putText(frame, "Left arm less than 65% accurate", (15, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

            
              # left arm
            angle = detector.findAngle(frame,11, 13, 15, 17, 19)
            per = np.interp(angle, (185 , 200), (0, 100))
            if (per >= 50):
                if(per <= 100):
                    #user's right side
                    cv2.putText(frame, "Right arm accurate 65%", (350, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
            
            elif(per < 50):
                cv2.putText(frame, "Right arm less than 65% accurate", (350, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)



              # left leg
            angle = detector.findAngle(frame, 23, 25, 27, 29, 31)
            per = np.interp(angle, (165, 180), (0, 100))
            if (per >= 50):
                if(per <= 100):
                    #user's left side
                    cv2.putText(frame, "Right leg accurate 65%", (350, 450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

            elif(per < 50):
                cv2.putText(frame, "Right leg less than 65% accurate", (350, 450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)



              # right leg
            angle = detector.findAngle(frame, 24, 26, 28,30, 32)
            per = np.interp(angle, (165, 180), (0, 100))
            if (per >= 50):
                if(per <= 100):
                    #user's right side
                    cv2.putText(frame, "Left leg accurate 65%", (15, 450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

            elif(per < 50):
                cv2.putText(frame, "Left leg less than 65% accurate", (15, 450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

           
           
           ret, buffer =  cv2.imencode('.jpg', frame)
           frame = buffer.tobytes()

           yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
           

def revolved_generate_frames():
    while True:
        #read the camera frames
        success, frame = cap.read()
        if not success:
            break

        #display the frames in buffer bytes in webpage
        else:
           img = cv2.resize(frame, (1280, 728))
           img = detector.findPose(frame)

           #this copying img content in frame to display
           frame = img.copy()
           lmlist = detector.getPosition(frame, False)
        #    print(lmlist)
           if len(lmlist) != 0:
               # right arm
            angle = detector.findAngle(frame, 12, 14, 16, 18, 20)
            per = np.interp(angle, (-15, -30), (0,100))
            if (per >= 50):
                if(per <= 100):
                    #user's left side
                    cv2.putText(frame, "Left arm accurate 65%", (15, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

            elif(per < 50):
                cv2.putText(frame, "Left arm less than 65% accurate", (15, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

            
              # left arm
            angle = detector.findAngle(frame,11, 13, 15, 17, 19)
            per = np.interp(angle, (25 , 40), (0, 100))
            if (per >= 50):
                if(per <= 100):
                    #user's right side
                    cv2.putText(frame, "Right arm accurate 65%", (350, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
            
            elif(per < 50):
                cv2.putText(frame, "Right arm less than 65% accurate", (350, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)



              # left leg
            angle = detector.findAngle(frame, 23, 25, 27, 29, 31)
            per = np.interp(angle, (185, 200), (0, 100))
            if (per >= 50):
                if(per <= 100):
                    #user's left side
                    cv2.putText(frame, "Right leg accurate 65%", (350, 450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

            elif(per < 50):
                cv2.putText(frame, "Right leg less than 65% accurate", (350, 450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)



              # right leg
            angle = detector.findAngle(frame, 24, 26, 28,30, 32)
            per = np.interp(angle, (255, 270), (0, 100))
            if (per >= 50):
                if(per <= 100):
                    #user's right side
                    cv2.putText(frame, "Left leg accurate 65%", (15, 450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

            elif(per < 50):
                cv2.putText(frame, "Left leg less than 65% accurate", (15, 450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

           
           
           ret, buffer =  cv2.imencode('.jpg', frame)
           frame = buffer.tobytes()

           yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
           
#change
def Butterfly_generate_frames():
    while True:
        #read the camera frames
        success, frame = cap.read()
        if not success:
            break

        #display the frames in buffer bytes in webpage
        else:
           img = cv2.resize(frame, (1280, 728))
           img = detector.findPose(frame)

           #this copying img content in frame to display
           frame = img.copy()
           lmlist = detector.getPosition(frame, False)
        #    print(lmlist)
           if len(lmlist) != 0:
               # right arm
            angle = detector.findAngle(frame, 12, 14, 16, 18, 20)
            per = np.interp(angle, (185, 195), (0,100))
            if (per >= 50):
                if(per <= 100):
                    #user's left side
                    cv2.putText(frame, "Left arm accurate 65%", (15, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

            elif(per < 50):
                cv2.putText(frame, "Left arm less than 65% accurate", (15, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

            
              # left arm
            angle = detector.findAngle(frame,11, 13, 15, 17, 19)
            per = np.interp(angle, (165 , 200), (0, 100))
            if (per >= 50):
                if(per <= 100):
                    #user's right side
                    cv2.putText(frame, "Right arm accurate 65%", (350, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
            
            elif(per < 50):
                cv2.putText(frame, "Right arm less than 65% accurate", (350, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)



              # left leg
            angle = detector.findAngle(frame, 23, 25, 27, 29, 31)
            per = np.interp(angle, (10, 20), (0, 100))
            if (per >= 50):
                if(per <= 100):
                    #user's left side
                    cv2.putText(frame, "Right leg accurate 65%", (350, 450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

            elif(per < 50):
                cv2.putText(frame, "Right leg less than 65% accurate", (350, 450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)



              # right leg
            angle = detector.findAngle(frame, 24, 26, 28,30, 32)
            per = np.interp(angle, (-5, -20), (0, 100))
            if (per >= 50):
                if(per <= 100):
                    #user's right side
                    cv2.putText(frame, "Left leg accurate 65%", (15, 450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

            elif(per < 50):
                cv2.putText(frame, "Left leg less than 65% accurate", (15, 450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

           
           
           ret, buffer =  cv2.imencode('.jpg', frame)
           frame = buffer.tobytes()

           yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
           
#change
def Bridge_generate_frames():
    while True:
        #read the camera frames
        success, frame = cap.read()
        if not success:
            break

        #display the frames in buffer bytes in webpage
        else:
           img = cv2.resize(frame, (1280, 728))
           img = detector.findPose(frame)

           #this copying img content in frame to display
           frame = img.copy()
           lmlist = detector.getPosition(frame, False)
        #    print(lmlist)
           if len(lmlist) != 0:
               # right arm
            angle = detector.findAngle(frame, 12, 14, 16, 18, 20)
            per = np.interp(angle, (170, 185), (0,100))
            if (per >= 50):
                if(per <= 100):
                    #user's left side
                    cv2.putText(frame, "Left arm accurate 65%", (15, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

            elif(per < 50):
                cv2.putText(frame, "Left arm less than 65% accurate", (15, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

            
              # left arm
            angle = detector.findAngle(frame,11, 13, 15, 17, 19)
            per = np.interp(angle, (165 , 280), (0, 100))
            if (per >= 50):
                if(per <= 100):
                    #user's right side
                    cv2.putText(frame, "Right arm accurate 65%", (350, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
            
            elif(per < 50):
                cv2.putText(frame, "Right arm less than 65% accurate", (350, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)



              # left leg
            angle = detector.findAngle(frame, 23, 25, 27, 29, 31)
            per = np.interp(angle, (60, 75), (0, 100))
            if (per >= 50):
                if(per <= 100):
                    #user's left side
                    cv2.putText(frame, "Right leg accurate 65%", (350, 450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

            elif(per < 50):
                cv2.putText(frame, "Right leg less than 65% accurate", (350, 450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)



              # right leg
            angle = detector.findAngle(frame, 24, 26, 28,30, 32)
            per = np.interp(angle, (50, 65), (0, 100))
            if (per >= 50):
                if(per <= 100):
                    #user's right side
                    cv2.putText(frame, "Left leg accurate 65%", (15, 450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

            elif(per < 50):
                cv2.putText(frame, "Left leg less than 65% accurate", (15, 450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

           
           
           ret, buffer =  cv2.imencode('.jpg', frame)
           frame = buffer.tobytes()

           yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
           

def Warrior2_generate_frames():
    while True:
        #read the camera frames
        success, frame = cap.read()
        if not success:
            break

        #display the frames in buffer bytes in webpage
        else:
           img = cv2.resize(frame, (1280, 728))
           img = detector.findPose(frame)

           #this copying img content in frame to display
           frame = img.copy()
           lmlist = detector.getPosition(frame, False)
        #    print(lmlist)
           if len(lmlist) != 0:
               # right arm
            angle = detector.findAngle(frame, 12, 14, 16, 18, 20)
            per = np.interp(angle, (175, 180), (0,100))
            if (per >= 50):
                if(per <= 100):
                    #user's left side
                    cv2.putText(frame, "Left arm accurate 65%", (15, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

            elif(per < 50):
                cv2.putText(frame, "Left arm less than 65% accurate", (15, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

            
              # left arm
            angle = detector.findAngle(frame,11, 13, 15, 17, 19)
            per = np.interp(angle, (-165 , -180), (0, 100))
            if (per >= 50):
                if(per <= 100):
                    #user's right side
                    cv2.putText(frame, "Right arm accurate 65%", (350, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
            
            elif(per < 50):
                cv2.putText(frame, "Right arm less than 65% accurate", (350, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)



              # left leg
            angle = detector.findAngle(frame, 23, 25, 27, 29, 31)
            per = np.interp(angle, (95, 115), (0, 100))
            if (per >= 50):
                if(per <= 100):
                    #user's left side
                    cv2.putText(frame, "Right leg accurate 65%", (350, 450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

            elif(per < 50):
                cv2.putText(frame, "Right leg less than 65% accurate", (350, 450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)



              # right leg
            angle = detector.findAngle(frame, 24, 26, 28,30, 32)
            per = np.interp(angle, (170, 185), (0, 100))
            if (per >= 50):
                if(per <= 100):
                    #user's right side
                    cv2.putText(frame, "Left leg accurate 65%", (15, 450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

            elif(per < 50):
                cv2.putText(frame, "Left leg less than 65% accurate", (15, 450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

           
           
           ret, buffer =  cv2.imencode('.jpg', frame)
           frame = buffer.tobytes()

           yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
           

def Bound_generate_frames():
    while True:
        #read the camera frames
        success, frame = cap.read()
        if not success:
            break

        #display the frames in buffer bytes in webpage
        else:
           img = cv2.resize(frame, (1280, 728))
           img = detector.findPose(frame)

           #this copying img content in frame to display
           frame = img.copy()
           lmlist = detector.getPosition(frame, False)
        #    print(lmlist)
           if len(lmlist) != 0:
               # right arm
            angle = detector.findAngle(frame, 12, 14, 16, 18, 20)
            per = np.interp(angle, (185, 200), (0,100))
            if (per >= 50):
                if(per <= 100):
                    #user's left side
                    cv2.putText(frame, "Left arm accurate 65%", (15, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

            elif(per < 50):
                cv2.putText(frame, "Left arm less than 65% accurate", (15, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

            
              # left arm
            angle = detector.findAngle(frame,11, 13, 15, 17, 19)
            per = np.interp(angle, (145 , 160), (0, 100))
            if (per >= 50):
                if(per <= 100):
                    #user's right side
                    cv2.putText(frame, "Right arm accurate 65%", (350, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
            
            elif(per < 50):
                cv2.putText(frame, "Right arm less than 65% accurate", (350, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)



              # left leg
            angle = detector.findAngle(frame, 23, 25, 27, 29, 31)
            per = np.interp(angle, (-10, -25), (0, 100))
            if (per >= 50):
                if(per <= 100):
                    #user's left side
                    cv2.putText(frame, "Right leg accurate 65%", (350, 450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

            elif(per < 50):
                cv2.putText(frame, "Right leg less than 65% accurate", (350, 450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)



              # right leg
            angle = detector.findAngle(frame, 24, 26, 28,30, 32)
            per = np.interp(angle, (15, 30), (0, 100))
            if (per >= 50):
                if(per <= 100):
                    #user's right side
                    cv2.putText(frame, "Left leg accurate 65%", (15, 450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

            elif(per < 50):
                cv2.putText(frame, "Left leg less than 65% accurate", (15, 450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

           
           
           ret, buffer =  cv2.imencode('.jpg', frame)
           frame = buffer.tobytes()

           yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
           

def wheel_generate_frames():
    while True:
        #read the camera frames
        success, frame = cap.read()
        if not success:
            break

        #display the frames in buffer bytes in webpage
        else:
           img = cv2.resize(frame, (1280, 728))
           img = detector.findPose(frame)

           #this copying img content in frame to display
           frame = img.copy()
           lmlist = detector.getPosition(frame, False)
        #    print(lmlist)
           if len(lmlist) != 0:
               # right arm
            angle = detector.findAngle(frame, 12, 14, 16, 18, 20)
            per = np.interp(angle, (185, 200), (0,100))
            if (per >= 50):
                if(per <= 100):
                    #user's left side
                    cv2.putText(frame, "Left arm accurate 65%", (15, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

            elif(per < 50):
                cv2.putText(frame, "Left arm less than 65% accurate", (15, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

            
              # left arm
            angle = detector.findAngle(frame,11, 13, 15, 17, 19)
            per = np.interp(angle, (175 , 190), (0, 100))
            if (per >= 50):
                if(per <= 100):
                    #user's right side
                    cv2.putText(frame, "Right arm accurate 65%", (350, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
            
            elif(per < 50):
                cv2.putText(frame, "Right arm less than 65% accurate", (350, 30), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)



              # left leg
            angle = detector.findAngle(frame, 23, 25, 27, 29, 31)
            per = np.interp(angle, (115, 130), (0, 100))
            if (per >= 50):
                if(per <= 100):
                    #user's left side
                    cv2.putText(frame, "Right leg accurate 65%", (350, 450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

            elif(per < 50):
                cv2.putText(frame, "Right leg less than 65% accurate", (350, 450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)



              # right leg
            angle = detector.findAngle(frame, 24, 26, 28,30, 32)
            per = np.interp(angle, (115, 130), (0, 100))
            if (per >= 50):
                if(per <= 100):
                    #user's right side
                    cv2.putText(frame, "Left leg accurate 65%", (15, 450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

            elif(per < 50):
                cv2.putText(frame, "Left leg less than 65% accurate", (15, 450), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)

           
           
           ret, buffer =  cv2.imencode('.jpg', frame)
           frame = buffer.tobytes()

           yield(b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')





login_manager = LoginManager()
login_manager.init_app(app)










# database:-

# Register 
class User_data(db.Model, UserMixin):
    def get_id(self):
           return (self.ID)
    ID = db.Column(db.Integer, primary_key=True)
    User_name = db.Column(db.String(100), nullable=False)
    Email = db.Column(db.String(200), nullable=False)
    Password = db.Column(db.String(100), nullable=False) 
    Confirm_pass = db.Column(db.String(100), nullable=False)

    # to display username on screen

    def __repr__(self) -> str:
        return '<User %r>' % self.User_name
    
    




@login_manager.user_loader
def load_user(user_id):
    return User_data.query.get(user_id)



@app.route('/')
def index():
    return render_template('index.html')


#login 

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        uemail = request.form["uemail"]
        upass = request.form["upass"]

        login = User_data.query.filter_by(Email=uemail,Password = upass).first()
        if login is not None:
            login_user(login)
            return redirect(url_for("index"))
        
        else:
            flash("Invalid Credentials!", "Warning")
    
    return render_template('login.html')

#Register

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        uname = request.form['uname']
        uemail = request.form['uemail']
        upass = request.form['upass']
        ucon_pass = request.form['ucon_pass']

        register = User_data(User_name=uname, Email=uemail, Password=upass, Confirm_pass=ucon_pass)
        db.session.add(register)
        db.session.commit()

        return redirect(url_for("login"))
    return render_template('register.html')


#logout:-

@app.route('/logout')
def logout():
    logout_user()
    return redirect('/')




@app.route('/reg_result')
def reg_result():
    return render_template('register.html')

@app.route('/Blog')
def Blog():
    return render_template('Blog.html')

@app.route('/About')
def About():
    return render_template('About.html')

@app.route('/Contact')
def Contact():
    return render_template('Contact.html')

@app.route('/select')
def select():
    return render_template('select.html')

@app.route('/tutorials')
def tutorials():
    return render_template('tutorials.html')

@app.route('/game')
def game():
    return render_template('game.html')

@app.route('/tracks')
def tracks():
    return render_template('tracks.html')

@app.route('/Yoga')
def Yoga():
    return render_template('Yoga.html')

@app.route('/intermediate')
def intermediate():
    return render_template('intermediate.html')

@app.route('/advance')
def advance():
    return render_template('advance.html')

@app.route('/Poses')
def Poses():
    return render_template('Poses.html')

@app.route('/Poses1')
def Poses1():
    return render_template('Poses1.html')

@app.route('/Poses2')
def Poses2():
    return render_template('Poses2.html')

@app.route('/Poses3')
def Poses3():
    return render_template('Poses3.html')

@app.route('/Poses4')
def Poses4():
    return render_template('Poses4.html')

@app.route('/Poses5')
def Poses5():
    return render_template('Poses5.html')

@app.route('/results')
def results():
    return render_template('results.html')

@app.route('/results1')
def results1():
    return render_template('results1.html')

@app.route('/results2')
def results2():
    return render_template('results2.html')

@app.route('/results3')
def results3():
    return render_template('results3.html')

@app.route('/results4')
def results4():
    return render_template('results4.html')

@app.route('/results5')
def results5():
    return render_template('results5.html')

@app.route('/iPoses1')
def iPoses1():
    return render_template('iPoses1.html')

@app.route('/iPoses2')
def iPoses2():
    return render_template('iPoses2.html')

@app.route('/iPoses3')
def iPoses3():
    return render_template('iPoses3.html')

@app.route('/iPoses4')
def iPoses4():
    return render_template('iPoses4.html')

@app.route('/iPoses5')
def iPoses5():
    return render_template('iPoses5.html')

@app.route('/iPoses6')
def iPoses6():
    return render_template('iPoses6.html')

@app.route('/iresults1')
def iresults1():
    return render_template('iresults1.html')

@app.route('/iresults2')
def iresults2():
    return render_template('iresults2.html')

@app.route('/iresults3')
def iresults3():
    return render_template('iresults3.html')

@app.route('/iresults4')
def iresults4():
    return render_template('iresults4.html')

@app.route('/iresults5')
def iresults5():
    return render_template('iresults5.html')

@app.route('/iresults6')
def iresults6():
    return render_template('iresults6.html')

@app.route('/aPoses1')
def aPoses1():
    return render_template('aPoses1.html')

@app.route('/aPoses2')
def aPoses2():
    return render_template('aPoses2.html')

@app.route('/aPoses3')
def aPoses3():
    return render_template('aPoses3.html')

@app.route('/aPoses4')
def aPoses4():
    return render_template('aPoses4.html')

@app.route('/aPoses5')
def aPoses5():
    return render_template('aPoses5.html')

@app.route('/aPoses6')
def aPoses6():
    return render_template('aPoses6.html')

@app.route('/aresults1')
def aresults1():
    return render_template('aresults1.html')

@app.route('/aresults2')
def aresults2():
    return render_template('aresults2.html')

@app.route('/aresults3')
def aresults3():
    return render_template('aresults3.html')

@app.route('/aresults4')
def aresults4():
    return render_template('aresults4.html')

@app.route('/aresults5')
def aresults5():
    return render_template('aresults5.html')

@app.route('/aresults6')
def aresults6():
    return render_template('aresults6.html')

@app.route('/video')
def video():
    return Response(palm_generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video1')
def video1():
    return Response(tree_generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video2')
def video2():
    return Response(triangle_generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video3')
def video3():
    return Response(warrior_generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video4')
def video4():
    return Response(dog_generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/video5')
def video5():
    return Response(mount_generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/ivideo1')
def ivideo1():
    return Response(cat_generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/ivideo2')
def ivideo2():
    return Response(camel_generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/ivideo3')
def ivideo3():
    return Response(sphinx_generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/ivideo4')
def ivideo4():
    return Response(corpse_generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/ivideo5')
def ivideo5():
    return Response(goddess_generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/ivideo6')
def ivideo6():
    return Response(cobras_generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/avideo1')
def avideo1():
    return Response(revolved_generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/avideo2')
def avideo2():
    return Response(Butterfly_generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/avideo3')
def avideo3():
    return Response(Bridge_generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/avideo4')
def avideo4():
    return Response(Warrior2_generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/avideo5')
def avideo5():
    return Response(Bound_generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/avideo6')
def avideo6():
    return Response(wheel_generate_frames(),mimetype='multipart/x-mixed-replace; boundary=frame')








if __name__ == "__main__":
    app.run(debug=True, port=8000)