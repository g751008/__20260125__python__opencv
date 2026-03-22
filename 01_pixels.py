import cv2
import  numpy as np

img1 = cv2.imread("images\gmap_arrow_small_56x72.jpg", 1)
img2 = cv2.imread("images\gmap_arrow_TINY.jpg", 1)
img3 = cv2.imread("images\gray_gmap_arrow.jpg", 1)
print(img1)
print(type(img1))
print(len(img1)) #72 height
print(len(img1[0])) #56 width
print(len(img1[0][0]))
print(img1[0][0])
print(img1.shape)
print(img1.dtype) #uint8(unsigned integer 8)
print(img1[6,28]) #類似img1[6][28]
print(img1[6,28,1]) #類似img1[6][28][1]
print(img1.size) #72*56*3
img1[4][28] = (0,0,0)
cv2.imwrite("images\01_pixels.jpg", img1)
img1[4][28] = (0,255,255)
cv2.imwrite("images\01_pixels_y.jpg", img1)
cv2.imwrite("images\01_pixels_y.png", img1)
img1[1:20][:] = (255,0,0)
img1[21:40][:] = (0,255,0)
img1[41:60][:] = (0,0,255)
cv2.imwrite("images\01_pixels_bgr.png", img1)

img1 = cv2.imread("images\gmap_arrow_small_56x72.jpg", 1)
img1[:len(img1)//2,len(img1[0])//2:] = (255,0,0)

cv2.imshow("Image", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
