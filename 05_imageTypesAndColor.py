import cv2
import numpy as np

color = cv2.imread("images/butterfly.jpg", 1)
#cv2.imshow("image", color)
print(color.shape)
height, width, channels = color.shape
print(cv2.split(color))
b,g,r= cv2.split(color)
#cv2.imshow("blue",b)
#cv2.imshow("green",g)
#cv2.imshow("red",r)
cv2.waitKey(0)
cv2.destroyAllWindows()

merged = cv2.merge([b,g,r])
#cv2.imshow("merged", merged)
cv2.waitKey(0)
cv2.destroyAllWindows()

new_r = np.zeros((height, width, 1) ,"uint8")
no_red = cv2.merge([b,g, new_r])
#cv2.imshow("combined no r",no_red)
cv2.waitKey(0)
cv2.destroyAllWindows()

bgr_split = np.empty([height, width*3, 3], "uint8")
cv2.imshow("bgr_split", bgr_split)
bgr_split[:,0:width] = cv2.merge([b,b,b])
bgr_split[:,width:width*2] = cv2.merge([g,g,g])
bgr_split[:,width*2:width*3] = cv2.merge([r,r,r])
cv2.imshow("bgr_split",bgr_split)
cv2.waitKey(0)
cv2.destroyAllWindows()

gray = cv2.cvtColor(color, cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(hsv)
hsv_split = np.concatenate((h,s,v), axis=1)
cv2.imshow("gray", gray)
cv2.imshow("hsv", hsv)
cv2.imshow("hsv split", hsv_split)
cv2.waitKey(0)
cv2.destroyAllWindows()