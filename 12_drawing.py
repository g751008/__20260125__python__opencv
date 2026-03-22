import numpy as np
import cv2

img = cv2.imread("images/transparent_butterfly.png", 1)

cv2.line(img, (100,100), (400,300), (0,0,255), 2)
cv2.rectangle(img, (100,100), (400,300), (255,0,0), 2) #厚度-1可畫成實心
cv2.circle(img, (230,90), 40, (0,255,0), -1) #厚度-1可畫成實心

cv2.imshow("New Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()