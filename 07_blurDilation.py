import cv2
import numpy as np

img = cv2.imread("images/blur_dilate_erode.png")
cv2.imshow("Image", img)

blur1 = cv2.GaussianBlur(img, (3,3),1)
cv2.imshow("blur1", blur1)

blur2 = cv2.GaussianBlur(img, (11,11),1)
cv2.imshow("blur2", blur2)

blur3 = cv2.GaussianBlur(img, (3,3),2)
cv2.imshow("blur3", blur3)

blur4 = cv2.GaussianBlur(img, (5,5),1)
cv2.imshow("blur4", blur4)

kernal = np.ones((5,5),"uint8")
dilate = cv2.dilate(img, kernal, iterations=1) #放大白色部位
cv2.imshow("dilate", dilate)
erode = cv2.erode(img, kernal, iterations=1) #放大黑色部位
cv2.imshow("erode", erode)

cv2.waitKey(0)
cv2.destroyAllWindows()