import cv2
import numpy as np

img=cv2.imread("messi5.jpg")

print(img.shape)
imgresize=cv2.resize(img,(300,200))
print(imgresize.shape)

imgCropped=img[0:200,200:400]


cv2.imshow("imageresiz",imgresize)
cv2.imshow("Image",img)
cv2.imshow("imgCropped",imgCropped)
cv2.waitKey(0)