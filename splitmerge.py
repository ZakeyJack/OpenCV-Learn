import cv2 as cv
import numpy as np

full_img = cv.imread('Photos/cantikku_5.JPG')
img = cv.resize(full_img, (0,0), fx=0.07, fy=0.07)
cv.imshow('Gambar', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

b, g, r = cv.split(img)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('B', b)
cv.imshow('G', g)
cv.imshow('R', r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

merged = cv.merge([b,g,r])
cv.imshow('Merged Image', merged)

cv.waitKey(0)