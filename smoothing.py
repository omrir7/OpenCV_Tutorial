import cv2 as cv
import numpy as np
dog = cv.imread("C:/Users/omrir/PycharmProjects/OpenCV_Tutorial/Images/dog1.jpg")
cv.imshow('dog',dog)

#Averaging
averaged = cv.blur(dog, (3,3))
cv.imshow('avg',averaged)

#Gaussian
gaus = cv.GaussianBlur(dog,(3,3),0)
cv.imshow('gaus',gaus)

#Median
median = cv.medianBlur(dog,3)
cv.imshow('med',median)

#Bilateral
Bilateral = cv.bilateralFilter(dog,10,50,50)
cv.imshow('bil',Bilateral)
cv.waitKey(0)