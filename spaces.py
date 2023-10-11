import cv2 as cv
import matplotlib.pyplot as plt

full_img = cv.imread('Photos/cantikku_5.JPG')
img = cv.resize(full_img, (0,0), fx=0.07, fy=0.07)
cv.imshow('Gambar', img)

# BGR to Grayscale
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', grey)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

# BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR to HLS
hls = cv.cvtColor(img, cv.COLOR_BGR2HLS)
cv.imshow('HLS', hls)

# BGR to LAB
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

# BGR to LUV
luv = cv.cvtColor(img, cv.COLOR_BGR2LUV)
cv.imshow('LUV', luv)

# BGR to XYZ
xyz = cv.cvtColor(img, cv.COLOR_BGR2XYZ)
cv.imshow('XYZ', xyz)

# BGR to YCrCb
ycrcb = cv.cvtColor(img, cv.COLOR_BGR2YCrCb)
cv.imshow('YCrCb', ycrcb)

# HSV to Grayscale
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
bgr_gray = cv.cvtColor(hsv_bgr, cv.COLOR_BGR2GRAY)
cv.imshow('HSV Gray', bgr_gray)


'''
Note:
    - BGR = Blue, Green, Red
    - RGB = Red, Green, Blue
    - Gray = Grayscale
    - HSV = Hue, Saturation, Value
    - HLS = Hue, Lightness, Saturation
    - LAB = Lightness, A, B
    - LUV = Lightness, U, V
    - XYZ = X, Y, Z
    - YCrCb = Y, Cr, Cb
From list above, we can't convert from Grayscale to HSV, HLS, LAB, LUV, XYZ, and YCrCb immediately.
We need to convert from Grayscale to BGR first.
Then, we can convert from BGR to HSV, HLS, LAB, LUV, XYZ, and YCrCb.
Vice versa, we can't convert from HSV, HLS, LAB, LUV, XYZ, and YCrCb to Grayscale immediately.
'''

plt.imshow(rgb)
plt.show()
'''
plt will showing reverse color. This happens because OpenCV uses BGR color scheme, while matplotlib uses RGB color scheme.
If we wan
'''

cv.waitKey(0)