import cv2
import numpy as np 

img = cv2.imread('box.png')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 155, 255, 0)
cv2.imshow('original', img)

_, contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (0,0,255), 2)

cv2.imshow('draw_contours', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
