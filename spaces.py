import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
dog = cv.imread("C:/Users/omrir/PycharmProjects/OpenCV_Tutorial/Images/dog1.jpg")
cv.imshow('dog',dog)

#BGR->Grey
gray = cv.cvtColor(dog,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

#BGR->HSV
hsv=cv.cvtColor(dog,cv.COLOR_BGR2HSV)
cv.imshow('hsv',hsv)

#BGR->LAB
lab = cv.cvtColor(dog,cv.COLOR_BGR2Lab)
cv.imshow('lab',lab)
#RGB
plt.imshow(dog)
plt.show()
#BGR->RGB
rgb = cv.cvtColor(dog,cv.COLOR_BGR2RGB)
cv.imshow('rgb',rgb)
cv.waitKey(0)

