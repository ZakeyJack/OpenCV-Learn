import cv2 as cv
import numpy as np

blank = np.zeros((400, 400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)

cv.imshow('Rectangle', rectangle)
cv.imshow('Cricle', circle)

# Bitwise AND
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('Bitwise AND', bitwise_and)

# Bitwise OR
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('Bitwise OR', bitwise_or)

# Bitwise XOR
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('Bitwise XOR', bitwise_xor)

# Bitwise NOT
bitwise_not_rect = cv.bitwise_not(rectangle)
bitwise_not_circle = cv.bitwise_not(circle)
bitwise_not_bitwise_and = cv.bitwise_not(bitwise_and)
bitwise_not_bitwise_or = cv.bitwise_not(bitwise_or)
bitwise_not_bitwise_xor = cv.bitwise_not(bitwise_xor)
cv.imshow('Bitwise NOT Rectangle', bitwise_not_rect)
cv.imshow('Bitwise NOT Circle', bitwise_not_circle)
cv.imshow('Bitwise NOT Bitwise AND', bitwise_not_bitwise_and)
cv.imshow('Bitwise NOT Bitwise OR', bitwise_not_bitwise_or)
cv.imshow('Bitwise NOT Bitwise XOR', bitwise_not_bitwise_xor)

cv.waitKey(0)