import numpy as np
import cv2

img = cv2.imread("images/sudoku.jpg", 0)
ret, thresh = cv2.threshold(img, 70, 255, cv2.THRESH_BINARY)
adapt_mean = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 21, 7) #blocksize一定要是奇數
adapt_gauss = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 7)

cv2.imshow("Original", img)
cv2.imshow("Thresh", thresh)
cv2.imshow("AdaptMean", adapt_mean)
cv2.imshow("AdaptGauss", adapt_gauss)
cv2.waitKey(0)
cv2.destroyAllWindows()


