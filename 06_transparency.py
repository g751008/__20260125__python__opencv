import cv2
import numpy as np

img = cv2.imread("images/butterfly.jpg", 1)
cv2.imshow("Original",img)

height, width , channels = img.shape
b,g,r = cv2.split(img)
a=np.zeros((height, width), "uint8")
a+=128
bgra = cv2.merge([b,g,r,a])
cv2.imwrite("images/transparent_butterfly.png", bgra)



cv2.waitKey(0)
cv2.destroyAllWindows()