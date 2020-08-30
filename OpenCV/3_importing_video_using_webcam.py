import cv2

cap = cv2.VideoCapture(0)
# here we have passed '0' as the parameter meaning that we want to use the default webcam as the input

cap.set(3,640) # setting the width to 640
cap.set(4,480) # setting the height to 480
cap.set(10,100) # setting the brightness

while True:
    success, img = cap.read()
    cv2.imshow('video',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break # press 'q' to break out of the video

print('WebCam working')