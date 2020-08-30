import cv2
import numpy as np

# 0 means black
# 1 means white

img_black = np.zeros((640,480)) # this is a grayscale img since it has only 2 dimensions
print(img_black.shape)

img_black = np.zeros((640,480,3),np.uint8) # this is a not a grayscale img since it has only 3 dimensions
# here 640 is the height and 480 is the width
print(img_black.shape)
# cv2.imshow('Black img',img_black)

img = np.zeros((640,480,3),np.uint8)
img[:] = 255,0,0 # : means that we want the entire img to be of that color
# we can also color a particular part of the img by specifying the height and width range
cv2.imshow('image',img)

cv2.line(img_black,(0,0),(300,300),(0,255,0),3)
# this means that a green line of thickness 3 is to be drawn from (0,0) to (300,300)

cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),3)
# here since we are passing coordinates we have to follow the format (width,height)

cv2.rectangle(img,(0,0),(300,400),(0,0,255),2)

img_filled = np.zeros((640,480,3),np.uint8)
cv2.rectangle(img_filled,(0,0),(300,400),(0,0,255),cv2.FILLED)
cv2.imshow('Filled image',img_filled)

cv2.circle(img,(400,50),30,(255,0,255),5)

cv2.putText(img,'OpenCV shapes & text',(50,100),cv2.FONT_HERSHEY_COMPLEX,1,(0,200,0),2)

cv2.imshow('Black img',img_black)
cv2.imshow('image',img)
cv2.waitKey(0)
