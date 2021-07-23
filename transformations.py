import numpy as np

import cv2 as cv
import numpy as np
dog = cv.imread('C:/Users/omrir/Desktop/Personal Projects/Images/dog.jpg')
cv.imshow('dog',dog)

#translation -x/y moving--------------------------
def translate(img,x,y): #-x-left,-y-up,
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)

translated = translate(dog,-100,100)
#cv.imshow('trans',translated)

#Rotation----------------------------------------
def rotate (img,angle,rotPoint = None):
    (hight,width) = img.shape[:2]
    if rotPoint==None:
        rotPoint = (width//2,hight//2)
    rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimension = (width,hight)
    return cv.warpAffine(img,rotMat,dimension)

rotated = rotate(dog,180)
#cv.imshow('rot',rotated)

#Flipping---------------------------------------
flip = cv.flip(dog,0)
#cv.imshow('flip',flip)
cv.waitKey(0)


cv.waitKey(0)