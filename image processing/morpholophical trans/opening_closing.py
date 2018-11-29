import cv2
import numpy as np 

img = cv2.imread('opening.png', 0)
img2 = cv2.imread('closing.png', 0)
line = cv2.imread('line.png', 0)

kernell = np.ones((9,3), np.uint8)
kernel = np.ones((5,5), np.uint8)

# open = dilate(erode)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
openingl = cv2.morphologyEx(line, cv2.MORPH_OPEN, kernell)

# close = erode(dilate)
closing = cv2.morphologyEx(img2, cv2.MORPH_CLOSE, kernel)

cv2.imshow('original', img)
cv2.imshow('opening', opening)
cv2.imshow('original2', img2)
cv2.imshow('closing', closing)
cv2.imshow('line', line)
cv2.imshow('openingl', openingl)

cv2.waitKey(0)
cv2.destroyAllWindows()