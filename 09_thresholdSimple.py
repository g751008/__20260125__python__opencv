import numpy as np
import cv2

img = cv2.imread("images/coins.png", 0)
ret, thresh = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)

cv2.imshow("Original", img)
cv2.imshow("Thresh", thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()