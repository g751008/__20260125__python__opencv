import numpy as np
import cv2

img = cv2.imread("images\dogs.png", 1)
template  = cv2.imread("images\dog_head.png", 1)

cv2.imshow("Img", img)
cv2.imshow("Template", template)

result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
print(min_val, max_val, min_loc, max_loc)
cv2.circle(result, max_loc, 20,255,2)
cv2.imshow("Result", result)

cv2.waitKey(0)
cv2.destroyAllWindows()