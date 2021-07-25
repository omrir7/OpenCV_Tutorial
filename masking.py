import cv2 as cv
import numpy as np

dog = cv.imread("C:/Users/omrir/PycharmProjects/OpenCV_Tutorial/Images/me.jpg")
cv.imshow('dog',dog)
blank = np.zeros(dog.shape[:2],dtype='uint8')

mask1 = cv.circle(blank,(dog.shape[1]//4+25,dog.shape[0]//4+125),150,255,-1)
cv.imshow('mask',mask1)

masked = cv.bitwise_and(dog,dog,mask=mask1)
cv.imshow('masked',masked)

cv.waitKey(0)