import cv2 as cv

def rescaleFrame(frame,scale=0.75):
    width = int(frame.shape[1]*scale)
    hight = int(frame.shape[0]*scale)
    dimensions = (width,hight)

    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

def changeRes(width,hight,capture):
    #only live videos
    capture.set(3,width)
    capture.set(4,hight)