import cv2 as cv

me = cv.imread('Images/people.jpg')
cv.imshow('me',me)

gray = cv.cvtColor(me,cv.COLOR_BGR2GRAY)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

face_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=3)
print('number of faces is '+str(len(face_rect)))

for (x,y,w,h) in face_rect:
    cv.rectangle(me,(x,y),(x+w,y+h),(0,0,255),1)

cv.imshow('faces',me)
#Videos--------------------------------------------------
capture = cv.VideoCapture('Videos/face.gif') #0 is the webcam
while True:
    isTrue, frame = capture.read()
    frame_gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    face_rect_frame= haar_cascade.detectMultiScale(frame_gray,scaleFactor=1.15,minNeighbors=8)
    for (x, y, w, h) in face_rect_frame:
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 1)
    cv.imshow('vid',frame)
    if cv.waitKey(15) & 0xff==ord('s'):
        break
capture.release()
cv.destroyAllWindows()
cv.waitKey(0)