import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

dog = cv.imread('Images/dog1.jpg')
gray  = cv.cvtColor(dog,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

#laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('lap',lap)

#sobel
sobelx = cv.Sobel(gray,cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray,cv.CV_64F, 0, 1)

cv.imshow('sx',sobelx)
cv.imshow('sy',sobely)
combined_sobel = cv.bitwise_or(sobely,sobelx)
cv.imshow('com_sob',combined_sobel)

# canny - including sobel in its process
canny = cv.Canny(gray,150,175)
cv.imshow('canny',canny)

cv.waitKey(0)