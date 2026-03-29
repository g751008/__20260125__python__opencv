import cv2
import numpy as np

cap = cv2.VideoCapture("images\people_walking.avi")

width = int(cap.get(3))
height = int(cap.get(4))

cv2.VideoWriter("optical_flow_walking.avi", cv2.VideoWriter_fourcc("M","J","P","G"),30,(width,height))

color = np.random.randint(0,255,(100,3))
ret, prev_frame = cap.read()
prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)

mask = np.zeros_like(prev_frame)

feature_params = dict(maxCorners=100, qualityLevel=0.3, minDistance=7,blockSize=7)


cv2.goodFeaturesToTrack(prev_gray, mask=None)