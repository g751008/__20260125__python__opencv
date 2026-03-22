import numpy as np
import cv2

img = cv2.imread("images/faces.jpg", 1)
cv2.imshow("Original", img)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(hsv)

cv2.imshow("Hue",h)
cv2.imshow("Saturation",s)

ret, min_sat = cv2.threshold(s, 40,255,cv2.THRESH_BINARY)
cv2.imshow("ThreshSat", min_sat)

cv2.waitKey(0)
cv2.destroyAllWindows()