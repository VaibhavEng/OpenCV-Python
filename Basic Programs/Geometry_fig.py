import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
print(img)
img[:]=255,0,0


cv2.rectangle(img,(0,0),(200,200),(0,255,0),2)
cv2.circle(img,(200,200),(20),(0,0,255),1)
cv2.putText(img," OPENCV ",(300,100),cv2.FONT_HERSHEY_COMPLEX,0.5,(0,150,0),3)



cv2.imshow("Image",img)
cv2.waitKey(0)