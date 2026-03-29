import numpy as np
import cv2

img = cv2.imread("images/tomatoes.jpg")
cv2.imshow("Original", img)

b,g,r = cv2.split(img)
ret, thresh1 = cv2.threshold(r,180,255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(r,180,200, cv2.THRESH_BINARY)
ret, thresh3 = cv2.threshold(r,180,220, cv2.THRESH_BINARY)
ret, thresh4 = cv2.threshold(r,180,240, cv2.THRESH_BINARY)
cv2.imshow("1", thresh1)
cv2.imshow("2", thresh2)
cv2.imshow("3", thresh3)
cv2.imshow("4", thresh4)

hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h,s,v=cv2.split(hsv)
cv2.imshow("Hue", h)
cv2.imshow("Saturation", s)
cv2.imshow("V", v)

ret, thresh = cv2.threshold(h, 30,255,cv2.THRESH_BINARY_INV)
cv2.imshow("Thresh Hue",thresh)


edges = cv2.Canny(v,100,200,apertureSize=3)
edges_inv = 255 - edges
cv2.imshow("Edges", edges_inv)

kernel = np.ones((3,3),"uint8")
erode = cv2.erode(edges_inv, kernel, iterations=1)
cv2.imshow("Erode", erode)

canny_thresh = cv2.bitwise_and(erode, thresh)
cv2.imshow("CannyThresh", canny_thresh)


contours, hierarchy = cv2.findContours(canny_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
tomatoes = img.copy()
for c in contours:
    area = cv2.contourArea(c)
    if area > 300:
        cv2.drawContours(tomatoes, [c], 0, (255,255,255), 1)
        M = cv2.moments(c)
        cx = int(M["m10"]/M["m00"])
        cy = int(M["m01"]/M["m00"])
        cv2.circle(tomatoes, (cx,cy),3,(255,255,0),-1)

cv2.imshow("Tomatoes", tomatoes)

cv2.waitKey(0)
cv2.destroyAllWindows()