import cv2 as cv
import numpy as np

blank = np.zeros((400,400),dtype='uint8')

rectangle = cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
circle = cv.circle(blank.copy(),(200,200),200,255,-1)

cv.imshow('rect',rectangle)
cv.imshow('circ',circle)

#And
bit_and =cv.bitwise_and(rectangle,circle)
cv.imshow('and',bit_and)

#Or
bit_or = cv.bitwise_or(rectangle,circle)
cv.imshow('or',bit_or)

#XOR
bit_xor = cv.bitwise_xor(rectangle,circle)
cv.imshow('xor',bit_xor)

#Not
bit_not = cv.bitwise_not(rectangle)
cv.imshow('not',bit_not)

cv.waitKey(0)