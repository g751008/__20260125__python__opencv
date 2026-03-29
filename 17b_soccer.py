import numpy as np
import cv2

soccer_game = cv2.imread("images\soccer_game.jpg", 1)
template = cv2.imread("images\soccerball.jpg", 1)
cv2.imshow("SoccerGame", soccer_game)
cv2.imshow("Template", template)

result = cv2.matchTemplate(soccer_game, template, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
cv2.circle(result, max_loc, 20,255,2)
cv2.imshow("Result", result)

cv2.waitKey(0)
cv2.destroyAllWindows()