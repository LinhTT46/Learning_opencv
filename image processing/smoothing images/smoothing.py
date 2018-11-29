import cv2
import numpy as np 

img = cv2.imread('color.jpg')

M1 = np.ones((3,3), np.float32)/9
dst1 = cv2.filter2D(img, -1, M1)

M2 = np.array([[-1, -1, 0],[-1, 0, 1], [0, 1, 1]])
dst2 = cv2.filter2D(img, -1, M2)

blur = cv2.blur(img, (5,5))
b_gaussian = cv2.GaussianBlur(img, (5,5), 0)
b_median = cv2.medianBlur(img, 5)
b_bilateral = cv2.bilateralFilter(img, 5, 175, 175)

cv2.imshow('original', img)
cv2.imshow('averaging', dst1)
cv2.imshow('lala', dst2)
cv2.imshow('blur', blur)
cv2.imshow('gaussian', b_gaussian)
cv2.imshow('median', b_median)
cv2.imshow('bilateral', b_bilateral)
cv2.waitKey(0)
cv2.destroyAllWindows()