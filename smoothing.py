import cv2 as cv

full_img = cv.imread('Photos/ruas_jalan.png')
img = cv.resize(full_img, (0,0), fx=0.25, fy=0.25)
cv.imshow('Gambar', img)

# Averaging
average = cv.blur(img, (3,3))
cv.imshow('Average Blur', average)

# Gaussian Blur
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian Blur', gauss)

# Median Blur
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

# Bilateral Blur
bilateral = cv.bilateralFilter(img, 50, 70, 70)
cv.imshow('Bilateral Blur', bilateral)

bil_canny = cv.Canny(bilateral, 125, 175)
cv.imshow('Bilateral Canny', bil_canny)

cv.waitKey(0)