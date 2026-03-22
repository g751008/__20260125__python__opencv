import numpy as np
import cv2


img=cv2.imread("images/blobs.png",1)
cv2.imshow("Original", img)

#Gray Image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
height , width = gray.shape

#Thresholding
ret, thresh = cv2.threshold(gray, 20,255,cv2.THRESH_BINARY)
cv2.imshow("Thresh", thresh)

#Adapt Thresholding
adapt_thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 111, 1)
cv2.imshow("AdaptThresh", adapt_thresh)

#Contouring
contours, hierachy = cv2.findContours(gray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
canvas = np.zeros((height, width, 3), "uint8")

cv2.drawContours(canvas, contours, -1, (0,255,255), 2) #contourIdx=-1等於全部
cv2.imshow("AdaptThresh", adapt_thresh)
cv2.imshow("New Image", img)
cv2.imshow("canvas", canvas)

cv2.waitKey(0)
cv2.destroyAllWindows()