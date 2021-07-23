import cv2 as cv

dog = cv.imread('C:/Users/omrir/Desktop/Personal Projects/Images/dog.jpg')
cv.imshow('dog',dog)
#converting to greyscale--------------------------
gray = cv.cvtColor(dog,cv.COLOR_BGR2GRAY)
#cv.imshow('gray',gray)

#Blur an image------------------------------------
Gaussian_blur = cv.GaussianBlur(dog,(7,7),cv.BORDER_DEFAULT)
#Median_blur = cv.medianBlur(dog,3)
#cv.imshow('Gaussian_blur',Gaussian_blur)
#cv.imshow('mediam_blur',Median_blur)

#Edge Cascade-----------------------------------
canny = cv.Canny(dog,125,175)
#TO REDUCE THE EDGES apply it on a blured image
#cv.imshow('edge',canny)


#dialating----------------------------------------
dilated = cv.dilate(canny,(7,7),iterations=4)
#cv.imshow('dialated',dilated)

#eroding--------------------------------------
eroded = cv.erode(dilated,(7,7),iterations=4)
#cv.imshow('erode',eroded)

#resize-cubic is larging, are if smalling----------
resized = cv.resize(dog,(1000,1000),interpolation=cv.INTER_CUBIC)
#cv.imshow('resized',resized)

#cropping-------------------------------------
cropped = dog[200:300,0:800]
#cv.imshow('crop',cropped)

cv.waitKey(0)