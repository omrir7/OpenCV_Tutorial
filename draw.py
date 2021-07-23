import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype='uint8')

#paint the blank in a certain color (blue,green,red)
blank[200:300,200:300] = 0,0,255
#cv.imshow('blue',blank)
#draw rect
rectangle = cv.rectangle(blank,(blank.shape[0]//2,blank.shape[0]//2),(375,375),(0,255,0),thickness=-1)
#cv.imshow('rect',rectangle)
#draw a circle
circ = cv.circle(blank,(250,250),100,(0,0,255),thickness=-1)
#cv.imshow('circ',circ)
#line
cv.line(blank,(200,200),(250,250),(255,255,255),thickness=3)
#cv.imshow('line',blank)
#write text
cv.putText(blank,"hello",(255,255),cv.FONT_ITALIC,1.0,(0,255,0),thickness=2)
cv.imshow('text',blank)
cv.waitKey(0)