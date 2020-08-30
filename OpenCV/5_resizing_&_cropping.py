import cv2

img = cv2.imread('media/lena.png')
print('Original image',img.shape)
# prints the current dimensions/pixels of the image

imgResize = cv2.resize(img,(640,640)) # format (width,height)
print('Resized image',imgResize.shape)

# for cropping the image we just need to define the starting and the ending points
# of the height as well as the width of the image
imgCropped = img[0:200,200:500] # format [height,width]

cv2.imshow('image',img)
cv2.imshow('Resized image',imgResize)
cv2.imshow('Croppend image',imgCropped)
cv2.waitKey(0)

