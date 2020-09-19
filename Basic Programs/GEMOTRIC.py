import numpy as np
import cv2
img = cv2.imread('HappyFish.jpg', 1)



#img = cv2.line(img, (0,0), (255,255), (0, 0, 255), 10)
#img = cv2.arrowedLine(img, (0,0), (255,255), (255, 0, 0), 10)
img = cv2.rectangle(img, (0, 0), (510, 128), (0 ,255 , 0), 10)
cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()