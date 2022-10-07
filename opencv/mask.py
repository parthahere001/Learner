import cv2 as cv
import numpy as np



image=cv.imread('image/bg.jpg')

blank=np.zeros(image.shape[:2],dtype='uint8')

""" creating a circle at the centre of the image with radius of 200px """
circle=cv.circle(blank.copy(),(image.shape[1]//2,image.shape[0]//2),200,255,-1)

""" creating a rectangle """
rectangle=cv.rectangle(blank.copy(),(image.shape[1]//4,image.shape[0]//4),(image.shape[1]//2,image.shape[0]//2),255,-1)


weird=cv.bitwise_xor(rectangle,circle)


""" masking the image """
mask=cv.bitwise_and(image,image,mask=weird)
cv.imshow('mask',mask)


cv.waitKey(0)