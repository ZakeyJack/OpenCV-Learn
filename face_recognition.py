import cv2 as cv
import numpy as np
import os

haar_cascade = cv.CascadeClassifier('haar_face.xml')

people = ['Danting', 'Hongyu', 'Nnian', 'Yeha', 'YeonyuMilk', 'Yuzi Jiang Fish']

# features = np.load('features.npy', allow_pickle=True)
# labels = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

full_img = cv.imread('Photos/People/Validate/Yuzi Jiang Fish/Yuzi Jiang Fish_13.jpg')
img = cv.resize(full_img, (0, 0), fx=0.25, fy=0.25)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# detect the face in the image.
faces_rect = haar_cascade.detectMultiScale(gray, 1.1, 4)

for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h, x:x+w] # crop the face. y:y+h is the height of the face, x:x+w is the width of the face.

    label, confidence = face_recognizer.predict(faces_roi)
    print(f'Label = {people[label]} with a confidence of {confidence}')

    cv.putText(img, str(people[label]), (x,y-20), cv.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)

cv.imshow('Detected Face', img)
cv.waitKey(0)