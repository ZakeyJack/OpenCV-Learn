import cv2 as cv
import numpy as np

img = cv.imread('Photos/cantikku_6.JPG')
# cv.imshow('Gambar', img)

blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank)

# 1. Paint of the image a certain color
# blank[200:300, 300:400] = 0, 0, 255 # BGR
# cv.imshow('Red', blank)

# 2. Draw a rectangle
# cv.rectangle(blank, (100, 100), (500, 500), (0, 0, 255), thickness=10)
# cv.imshow('Rectangle', blank)
'''
From that command, this is the result:
    - blank = the image
    - (150, 150) = the starting point of the rectangle
    - (500, 500) = the ending point of the rectangle
    - (0, 0, 255) = the color of the rectangle with format BGR
    - thickness = the thickness of the rectangle
'''
# cv.rectangle(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), (0, 0, 255), thickness=-1)
# cv.imshow('Rectangle', blank)
'''
From that command, this is the result:
    - blank = the image
    - (0, 0) = the starting point of the rectangle
    - (blank.shape[1]//2, blank.shape[0]//2) = the ending point of the rectangle (the shape of the image is 500x500, so the ending point is 250x250)
    - (0, 0, 255) = the color of the rectangle with format BGR
    - thickness = the thickness of the rectangle
'''

# 3. Draw a circle
# cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0, 255, 0), thickness=-1)
# cv.imshow('Circle', blank)
'''
From that command, this is the result:
    - blank = the image
    - (blank.shape[1]//2, blank.shape[0]//2) = the center of the circle (the shape of the image is 500x500, so the center is 250x250)
    - 40 = the radius of the circle
    - (0, 0, 255) = the color of the circle with format BGR
    - thickness = the thickness of the circle
'''

# 4. Draw a line
# cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255, 255, 255), thickness=3)
# cv.imshow('Line', blank)
'''
From that command, this is the result:
    - blank = the image
    - (0, 0) = the starting point of the line
    - (blank.shape[1]//2, blank.shape[0]//2) = the ending point of the line (the shape of the image is 500x500, so the ending point is 250x250)
    - (255, 255, 255) = the color of the line with format BGR
    - thickness = the thickness of the line
'''
cv.putText(blank, 'Hey honey~', (150, 255), cv.FONT_HERSHEY_COMPLEX, 1.0, (0, 255, 0), 1)
cv.imshow('Text', blank)
'''
From that command, this is the result:
    - blank = the image
    - 'Hey honey~' = the text that will be written
    - (0, 255) = the starting point of the text
    - cv.FONT_HERSHEY_TRIPLEX = the font of the text
    - 1.0 = the scale of the text
    - (0, 255, 0) = the color of the text with format BGR
    - 1.0 = the thickness of the text
'''

cv.waitKey(0)