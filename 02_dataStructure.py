import cv2
import numpy as np
import random

img = np.zeros((400,800),"uint8") #黑白，較寬
black = np.zeros((500,500,3),"uint8")
black+=100
cv2.imshow("black", black)
print(black[0,0,:])

white = np.ones((500,500,3),"uint8")
white*=255
cv2.imshow("white", white)
print(white[0,0,:])

ones = np.ones((500,500,3),"uint8")
x = ones.copy()
ones2 = ones
ones2 *= 255
cv2.imshow("ones", ones)
cv2.imshow("ones2", ones2)
cv2.imshow("x", x)

cv2.waitKey(0)
cv2.destroyAllWindows()