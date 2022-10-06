import cv2 as cv

""" reading an image from image folder """
img=cv.imread('image/car.jpg') 

""" resizing the image to fit the window """
image=cv.resize(img,(1000,750),interpolation=cv.INTER_AREA)

""" showing original image """
cv.imshow('original',image)

""" converting the image to gray scale using in-built function """
gray=cv.cvtColor(image,cv.COLOR_BGR2GRAY)

""" showing the gray scale converted image """
cv.imshow('gray',gray)

""" This will show the output unless we press any key """
cv.waitKey(0)
