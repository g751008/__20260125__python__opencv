import numpy as np
import cv2

img = cv2.imread("images/butterfly.jpg", 1)
img_stretch = cv2.resize(img, (500,500))
img_half = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
img_double = cv2.resize(img, (0,0), fx=2, fy=2)
cv2.imshow("Original", img)
cv2.imshow("Resized", img_stretch)
cv2.imshow("Half", img_half)
cv2.imshow("Double", img_double)

#rotate image
height, width , channels = img.shape
matrix1 = cv2.getRotationMatrix2D((0,0),-30,1)
matrix2 = cv2.getRotationMatrix2D((width//2, height//2),-45,1)
img_rotated = cv2.warpAffine(img, matrix1, (width, height))
img_rotatedCenter = cv2.warpAffine(img, matrix2, (width, height))
cv2.imshow("Rotated", img_rotated)
cv2.imshow("RotatedCenter", img_rotatedCenter)

cv2.waitKey(0)
cv2.destroyAllWindows()