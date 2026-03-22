import numpy as np
import cv2

img = cv2.imread("images/coins.png", 1)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
height, width = gray.shape

binary = np.zeros((height, width), "uint8")
threshold = 100

for row in range(0, height):
    for col in range(0, width):
        if gray[row][col] > threshold:
            binary[row][col] = 255
        else:
            binary[row][col] = 0  


cv2.imshow("Original", img)
cv2.imshow("binary", binary)
cv2.waitKey(0)
cv2.destroyAllWindows()