import cv2 as cv
import numpy as np

full_img = cv.imread('Photos/cantikku_4.jpg')
img = cv.resize(full_img, (0, 0), fx=0.07, fy=0.07)
cv.imshow('Gambar', img)

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# # blur = cv.GaussianBlur(gray, (3,3), cv.BORDER_DEFAULT)
# # cv.imshow('Blur', blur)

# canny = cv.Canny(gray, 125, 175)
# cv.imshow('Canny', canny)

# ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
# cv.imshow('Thresh', thresh)

# contours1, hierarchies1 = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
# print(f'{len(contours1)} contour(s) found!')

# contours2, hierarchies2 = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
# print(f'{len(contours2)} contour(s) found!')

'''
That is the difference between the two methods.
The first one is the number of contours found in the image.
The second one is the number of contours found in the image after applying the Canny edge detection.
Contours are the boundaries of a shape with the same intensity.
They are a curve joining all the continuous points (along the boundary), having same color or intensity.
The contours are a useful tool for shape analysis and object detection and recognition.
The difference betweeb contours and edges is that edges are the discontinuities in the image intensity function.
'''

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

blur = cv.GaussianBlur(gray, (3,3), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny', canny)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)

contours1, hierarchies1 = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours1)} contour(s) found!')

contours2, hierarchies2 = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours2)} contour(s) found!')

cv.drawContours(blank, contours2, -1, (0,0,225), 1)
cv.imshow('Contours Drawn', blank)

cv.waitKey(0)