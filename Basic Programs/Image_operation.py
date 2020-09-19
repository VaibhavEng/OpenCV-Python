import cv2
import numpy as np

img = cv2.imread("lena.jpg")
kernel=np.ones((5,5),np.uint8)


imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBluer = cv2.GaussianBlur(imggray,(7,7),0)
imgcanny = cv2.Canny(img,150,200)
imgdialation=cv2.dilate(imgcanny,kernel,iterations=1)
imgEroded=cv2.erode(imgdialation,kernel,iterations=1)


cv2.imshow("Gray image",imggray)
cv2.imshow("Blur Image",imgBluer)
cv2.imshow("canny Image",imgcanny)
cv2.imshow("dialation  Image",imgdialation)
cv2.imshow("imgEroded Image",imgEroded)



cv2.waitKey(0)