import cv2

cap = cv2.VideoCapture('media/test_video.mp4')
# by this we have imported the video in the 'cap' object
# since a video is a sequence of images we will use a while loop to display the video

while True:
    success, img = cap.read()
    cv2.imshow('video',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break # press 'q' to break out of the video