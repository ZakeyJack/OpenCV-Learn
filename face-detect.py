import cv2 as cv

full_img = cv.imread('Photos/cantikku_15.jpg')
img = cv.resize(full_img, (0, 0), fx=0.08, fy=0.08)
cv.imshow('Original Image', img)

grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grey Image', grey)

haar_cascade = cv.CascadeClassifier('haar_face.xml')
faces_rect = haar_cascade.detectMultiScale(grey, scaleFactor=1.1, minNeighbors=5)

print(f'Number of faces found = {len(faces_rect)}')

for (x, y, w, h) in faces_rect:
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)

cv.imshow('Detected Face', img)

cv.waitKey(0)