import cv2

# img -> variable to store the imported image
img = cv2.imread('media/lena.png')
print('image imported ')
# now we have imported our image from the media folder

# now we need to display the image that we imported
cv2.imshow('Output',img)
print('image displayed ')
# here 'output' is the name of the window and 'img' is the name of the object that we want to display

# the image displayed but it went away to fast so we have to add a delay so that we are able to see the img
cv2.waitKey(5000) # 0 means an infinite delay
# we can also pass a number as parameter which means the output will be delayed by that many milliseconds








