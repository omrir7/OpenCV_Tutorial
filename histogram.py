import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


dog = cv.imread('Images/dog1.jpg')
cv.imshow('dog',dog)
blank = np.zeros(dog.shape[:2],dtype='uint8')
mask1 = cv.circle(blank,(dog.shape[1]//4+150,dog.shape[0]//4+50),150,255,-1)

gray = cv.cvtColor(dog,cv.COLOR_BGR2GRAY)
#cv.imshow('gray',gray)
gray_masked = cv.bitwise_and(gray,gray,mask = mask1)
#cv.imshow('gray_masked',gray_masked)
regular_masked = cv.bitwise_and(dog,dog,mask1)
#gray hist----------------------------------------------------
gray_hist = cv.calcHist([gray],[0],mask1,[256],[0,256])

#plt.figure()
#plt.title('GrayScale Hist')
#plt.xlabel('Bins')
#plt.ylabel('# of pixels')
#plt.plot(gray_hist)
#plt.xlim([0,256])
#plt.show()

#color histogram-----------------------------------------
colors = ('b','g','r')
for i,col in enumerate(colors):
    hist = cv.calcHist([dog],[i],None,[256],[0,256])
    plt.plot(hist,color=col)

plt.show()
cv.waitKey(0)