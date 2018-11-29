import cv2
import numpy as np 

img = cv2.imread('messi.jpg')

lower_reso = cv2.pyrDown(img)
lower_reso2 = cv2.pyrDown(lower_reso)
high_reso2 = cv2.pyrUp(lower_reso2)

cv2.imshow('original', img)
cv2.imshow('lower_reso', lower_reso)
cv2.imshow('lower_reso2', lower_reso2)
cv2.imshow('high_reso2', high_reso2)
cv2.waitKey(0)
cv2.destroyAllWindows()