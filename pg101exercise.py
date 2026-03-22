import cv2
import numpy as np

print(cv2.IMREAD_GRAYSCALE)
print(cv2.IMREAD_COLOR_RGB)

img = cv2.imread("images\cat1.jpg", 0) #黑白
img = cv2.imread("images\cat1.jpg", 1) #彩色

cv2.imshow("Cute Kitten", img)
cv2.imshow("Cute Kitten2", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


img = cv2.imread("images\dog1.jpg", 1) #彩色
cv2.imshow("Cute Dog", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

img = cv2.imread("images\cat2.jpg", 0) 
cv2.imshow("Cute Kitten", img)
cv2.waitKey(0)
cv2.destroyAllWindows()



img = cv2.imread("images\dog2.jpg", 0) 
cv2.imshow("Cute dog", img)
cv2.waitKey(0)
cv2.destroyAllWindows()