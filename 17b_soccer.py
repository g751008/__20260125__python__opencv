import numpy as np
import cv2

soccer_game = cv2.imread("images\soccer_game.jpg", 1)
template = cv2.imread("images\soccerball.jpg", 1)
height, width, channels = template.shape
cv2.imshow("SoccerGame", soccer_game)
cv2.imshow("Template", template)

result = cv2.matchTemplate(soccer_game, template, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
cv2.circle(result, max_loc, 30,255,2)
cv2.imshow("Result", result)

cv2.circle(soccer_game, (max_loc[0]+width//2, max_loc[1]+height//2), 30,(0,0,255),2)
cv2.imshow("Circled Soccerball", soccer_game)

img = cv2.imread("images\soccer_game.jpg", 1)
cv2.rectangle(img, max_loc,(max_loc[0]+width, max_loc[1]+height), (0,0,255),2)
cv2.imshow("Rectangled Soccerball", img)

cv2.waitKey(0)
cv2.destroyAllWindows()