import cv2
import numpy as np
import random

img = np.zeros((400,800),"uint8") #黑白，較寬
img = np.zeros((500,500,3),"uint8")
height, width, channel = img.shape

#畫星星
for i in range(0,50): 
    #x=random.randint(5,495)
    #y=random.randint(5,495)
    #x = random.randint(0, img.shape[1]-3)
    #y = random.randint(0, img.shape[0]-3)    
    x = random.randint(0, width-3)
    y = random.randint(0, height-3)
    img[y:y+2,x:x+2] = (255,255,255)

#畫太陽
img[20:40,20:40] = (0,255,255)

#畫海
img[height-100:,:] = (255,0,0)

#畫島
img[height-80:height-10,width-120:] = (0,150,0)

#畫樹
img[height-120:height-50,width-95:width-75] = (45,82,160)
img[height-160:height-120,width-120:width-50] = (0,150,0)

cv2.imshow("ZEROS Image", img)

blurred = cv2.GaussianBlur(img, (3,3) , 0)
cv2.imshow("blurred", blurred)

cv2.waitKey(0)
cv2.destroyAllWindows()