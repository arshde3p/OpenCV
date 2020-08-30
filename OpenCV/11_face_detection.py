import cv2
import numpy as np
cap = cv2.VideoCapture(0)
# here we have passed '0' as the parameter meaning that we want to use the default webcam as the input

cap.set(3,640) # setting the width to 640
cap.set(4,480) # setting the height to 480
cap.set(10,100) # setting the brightness

while True:
    success, img = cap.read()

    faceCascade = cv2.CascadeClassifier('media/haarcascade_frontalface_default.xml')
    # img = cv2.imread('media/lena.png')
    # imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0, 3))
    cv2.imshow('video',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break # press 'q' to break out of the video

# faceCascade = cv2.CascadeClassifier('media/haarcascade_frontalface_default.xml')
# img = cv2.imread('media/lena.png')
# imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#
# faces = faceCascade.detectMultiScale(imgGray,1.1,4)
# for (x,y,w,h) in faces:
#     cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0,3))

# cv2.imshow('lena',img)
# cv2.waitKey(0)