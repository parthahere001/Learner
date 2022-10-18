import cv2 as cv 
import numpy as np

""" reading an image """
img=cv.imread('image/bg.jpg')
 
""" resizing the image """
image=cv.resize(img,(1000,750),interpolation=cv.INTER_AREA)

""" converting an image in gray scale """
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

""" detecting the edges in the image """
canny=cv.Canny(gray,125,175)


""" detecting the contours in the gray image """
contours,hierarchies=cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)

print(f'{len(contours)} no of contours found')

""" creating an blank image to draw the contours on """
blank=np.zeros(img.shape,dtype='uint8')
cv.drawContours(blank,contours,-1,(0,0,255),1)
cv.imshow('contours',blank)

cv.waitKey(0)