import cv2 as cv
import numpy as np
dog = cv.imread("C:/Users/omrir/PycharmProjects/OpenCV_Tutorial/Images/me.jpg")
cv.imshow('dog',dog)

blank = np.zeros(dog.shape[:2],dtype='uint8')

b,g,r = cv.split(dog)
#show channels - in black and white
cv.imshow('b',b)
cv.imshow('g',g)
cv.imshow('r',r)

merged = cv.merge([b,g,r])
cv.imshow('merged',merged)
#show channels in the actual color of the channel
blue = cv.merge([b,blank,blank])
red = cv.merge([blank,blank,r])
green = cv.merge([blank,g,blank])

cv.imshow('blue',blue)
cv.imshow('red',red)
cv.imshow('green',green)


cv.waitKey(0)