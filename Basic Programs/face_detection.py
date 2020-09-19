import cv2
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
img = cv2.imread("lena.jpg")
imggray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imggray,1.1,4)

for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(250,0,0),2)

cv2.imshow("result",img)
cv2.waitKey(0)