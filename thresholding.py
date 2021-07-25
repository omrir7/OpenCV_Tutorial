import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

dog = cv.imread('Images/dog1.jpg')
gray  = cv.cvtColor(dog,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

#simple thresholding-------------------------------------------
threshold,thresh = cv.threshold(gray,155,255,cv.THRESH_BINARY)
cv.imshow('thresh',thresh)

threshold_inv,thresh_inv = cv.threshold(gray,155,255,cv.THRESH_BINARY_INV)
cv.imshow('thresh_int',thresh_inv)

#adaptive thresholding----------------------------------------
adap_thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,17,3)
cv.imshow('adap',adap_thresh)
cv.waitKey(0)