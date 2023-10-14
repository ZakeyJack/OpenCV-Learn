import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

full_img = cv.imread('Photos/cantikku_10.jpg')
img = cv.resize(full_img, (0,0), fx=0.125, fy=0.125)
cv.imshow('Original Image', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray Image', gray)

circle = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2-75), 125, 255, -1)
# mask = cv.bitwise_and(gray, gray, mask=circle)
# cv.imshow('Mask', mask)

# gray_hist = cv.calcHist([gray], [0], mask, [256], [0,256])

# # Grayscale Histogram
# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of Pixels')
# plt.xlim([0,256])
# plt.plot(gray_hist)
# plt.show()

# Color Histogram
mask = cv.bitwise_and(img, img, mask=circle)
cv.imshow('Mask', mask)

plt.figure()
plt.title('Color Histogram')
plt.xlabel('Bins')
plt.ylabel('# of Pixels')
color = ('b', 'g', 'r')

for i,col in enumerate(color):
    hist = cv.calcHist([img], [i], None, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])

plt.show()

cv.waitKey(0)