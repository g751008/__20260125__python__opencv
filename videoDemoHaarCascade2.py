import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while 1:
    ret, frame = cap.read()
    frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    path="haarcascade_frontalface_default.xml"
    face_cascade = cv2.CascadeClassifier(path)
    faces = face_cascade.detectMultiScale(frameGray, scaleFactor=1.05, minNeighbors=20, minSize=(50,50))

    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y),(x+w,y+h), (255,0,0),2)

        cv2.imshow("video stream", frame)
        cv2.waitKey(20)
        

