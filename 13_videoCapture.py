import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while 1:
    net, frame = cap.read()
    cv2.rectangle(frame, (100,200),(100,300),(255,0,0),2)
    cv2.imshow("Video", frame)    
    frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
    character = cv2.waitKey(20) #20毫秒
    if character & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()