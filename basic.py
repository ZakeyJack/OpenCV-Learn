import cv2 as cv

full_img = cv.imread('Photos/ruas_jalan.png')
# cv.imshow('Gambar', img)
img = cv.resize(full_img, (0, 0), fx=0.5, fy=0.5)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blur = cv.GaussianBlur(img, (5, 5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny', canny)

dilated = cv.dilate(canny, (7, 7), iterations=10)
cv.imshow('Dilated', dilated)

eroded = cv.erode(dilated, (7, 7), iterations=10)
cv.imshow('Eroded', eroded)

cv.waitKey(0)