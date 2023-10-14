import cv2 as cv
import numpy as np

full_img = cv.imread('Photos/ruas_area.jpg')
img = cv.resize(full_img, (0,0), fx=0.1, fy=0.1)
cv.imshow('Original Image', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
# cv.imshow('Blank Image', blank)

def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2, height//2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)

rect = cv.rectangle(blank.copy(), (0, img.shape[0]//4), (img.shape[1], img.shape[0]-75), 255, -1)
# cv.imshow('Mask', rect)

rect_rot = cv.rectangle(blank.copy(), (0, 0), (img.shape[1], img.shape[1]), 255, -1)
rect_rot_cw = rotate(rect_rot, 30)
# cv.imshow('Mask CW Rotated', rect_rot_cw)
rect_rot_ccw = rotate(rect_rot, -30)
# cv.imshow('Mask CCW Rotated', rect_rot_ccw)

combine_1 = cv.bitwise_and(rect_rot_cw, rect_rot_ccw)
# cv.imshow('Combine 1', combine_1)

small_rect = cv.rectangle(blank.copy(), (0, img.shape[0]//2), (img.shape[1], img.shape[0]-75), 255, -1)
# cv.imshow('Small Rectangle', small_rect)

combine_2 = cv.bitwise_or(combine_1, small_rect)
# cv.imshow('Combine 2', combine_2)

mask = cv.bitwise_and(rect, combine_2)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Masked Image', masked)

bilateral = cv.bilateralFilter(masked, 50, 70, 70)
cv.imshow('Bilateral Blur', bilateral)

canny = cv.Canny(bilateral, 125, 175)
cv.imshow('Canny', canny)

cv.waitKey(0)