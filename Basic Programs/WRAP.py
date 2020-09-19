import cv2
import numpy as np

img = cv2.imread("pic1.png")

width,height = 250,350
pts1 = np.float32([[252,87],[313,182],[323,39],[384,135]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix=cv2.getPerspectiveTransform(pts1,pts2)
imgoutput=cv2.warpPerspective(img,matrix,(width,height))


cv2.imshow("Output",imgoutput)




cv2.imshow("Image",img)
cv2.waitKey(0)