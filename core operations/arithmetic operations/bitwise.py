import cv2 
import numpy as np 
 
img1 = cv2.imread('messi.jpg')
img2 = cv2.imread('opencv.png')

# create roi
rows, cols = img2.shape[:2]
roi = img1[0: rows, 0: cols]

# create a mask of logo and create its inverse mask also
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
_, mask = cv2.threshold(img2gray, 50, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

# black-out the area of logo in roi
img1_bg = cv2.bitwise_and(roi, roi, mask = mask_inv)

# take only region of logo from logo image
img2_fg = cv2.bitwise_and(img2, img2, mask = mask)

# put logo in roi adn modify the main image
dst = cv2.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = dst

cv2.imshow('res', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()