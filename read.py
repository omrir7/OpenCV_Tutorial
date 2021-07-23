import cv2 as cv
from rescale import *

#Images
dog = cv.imread('C:/Users/omrir/Desktop/Personal Projects/Images/dog.jpg')
cv.imshow('Dog',dog)
#Videos
capture = cv.VideoCapture('C:/Users/omrir/Desktop/Personal Projects/Videos/short.mp4') #0 is the webcam
while True:
    isTrue, frame = capture.read()
    print(frame)
    cv.imshow('vid',frame)
    if cv.waitKey(20) & 0xff==ord('s'):
        break
capture.release()
cv.destroyAllWindows()

cv.waitKey(0) #wait for a delay for a key to be pressed
