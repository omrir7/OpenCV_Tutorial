import cv2 as cv
import numpy as np
me = cv.imread("C:/Users/omrir/PycharmProjects/OpenCV_Tutorial/Images/dog1.jpg")
cv.imshow('me',me)

blank = np.zeros(me.shape, dtype='uint8') #for contours drawing

gray = cv.cvtColor(me,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

#first method - BLUR----------------------------------------
blur = cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
#cv.imshow('blur',blur)

#canny = cv.Canny(blur,125,175)
#cv.imshow('canny',canny)
#contours, hierarchies = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)

#Second method - Threshoold-------------------------------
ret, tresh = cv.threshold(blur,125,255,cv.THRESH_BINARY) #pass blur,gray
contours, hierarchies = cv.findContours(tresh,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
cv.imshow('tresh',tresh)
print(f'{len(contours)} countours found!')

cv.drawContours(blank,contours,-1,(0,0,255),1)
cv.imshow('countours on blank',blank)
cv.waitKey(0)