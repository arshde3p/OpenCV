import cv2
import numpy as np

def empty(a):
    pass
def stackImages(scale,imgArray):
    rows = len(imgArray)
    cols = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[1]
    height = imgArray[0][0].shape[0]
    if rowsAvailable:
        for x in range ( 0, rows):
            for y in range(0, cols):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape [:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2: imgArray[x][y]= cv2.cvtColor( imgArray[x][y], cv2.COLOR_GRAY2BGR)
        imageBlank = np.zeros((height, width, 3), np.uint8)
        hor = [imageBlank]*rows
        hor_con = [imageBlank]*rows
        for x in range(0, rows):
            hor[x] = np.hstack(imgArray[x])
        ver = np.vstack(hor)
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None,scale, scale)
            if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
        hor= np.hstack(imgArray)
        ver = hor
    return ver

# trackbars help to find the optimum minimum and maximum values of the color
cv2.namedWindow('Trackbars')
cv2.resizeWindow('Trackbars',640,240)
cv2.createTrackbar('Hue_min','Trackbars',0,179,empty)
cv2.createTrackbar('Hue_max','Trackbars',179,179,empty)
cv2.createTrackbar('Sat_min','Trackbars',0,255,empty)
cv2.createTrackbar('Sat_max','Trackbars',255,255,empty)
cv2.createTrackbar('Val_min','Trackbars',0,255,empty)
cv2.createTrackbar('Val_max','Trackbars',255,255,empty)
cap = cv2.VideoCapture(0)

# cap.set(3,640) # setting the width to 640
# cap.set(4,480) # setting the height to 480
# cap.set(10,150) # setting the brightness
while True:
    img = cv2.imread('media/lambo.png')
    # success, img = cap.read()
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos('Hue_min', 'Trackbars')
    h_max = cv2.getTrackbarPos('Hue_max', 'Trackbars')
    s_min = cv2.getTrackbarPos('Sat_min', 'Trackbars')
    s_max = cv2.getTrackbarPos('Sat_max', 'Trackbars')
    v_min = cv2.getTrackbarPos('Val_min', 'Trackbars')
    v_max = cv2.getTrackbarPos('Val_max', 'Trackbars')
    print(h_min,h_max,s_min,s_max,v_min,v_max)
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV,lower,upper)
    imgResults = cv2.bitwise_and(img,img,mask=mask)
    # cv2.imshow('image',imgHSV)
    # cv2.imshow('Mask', mask)
    # cv2.imshow('Resulting image', imgResults)

    imgStack = stackImages(0.7, ([img,imgHSV],[mask,imgResults]))
    cv2.imshow('Stacked images', imgStack)
    cv2.waitKey(1)