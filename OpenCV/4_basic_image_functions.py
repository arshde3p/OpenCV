import cv2
import numpy as np

img = cv2.imread('media/lena.png')

kernel = np.ones((5,5),np.uint8)
# here we are declaring a (5,5) unit matrix of data type unsigned int (0,255)

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(15,15),0)
# here ksize (15,15) is the kernel size -> means the intensity of the blur

# to find the outlines of the image we will use the canny function
imgCanny = cv2.Canny(img,100,100)
# to change the sharpness of the imgCanny we can change the threshold value

imgDilation = cv2.dilate(imgCanny,kernel,iterations=1)

imgEroded = cv2.erode(imgDilation,kernel,iterations=1)

# cv2.imshow('Grayscale image',imgGray)
# cv2.imshow('Blur image',imgBlur)
cv2.imshow('Canny image',imgCanny)
cv2.imshow('Dilation image',imgDilation)
cv2.imshow('Eroded image',imgEroded)
cv2.waitKey(0)
