import cv2
import numpy as np 

img = cv2.imread('hand.png')
img = cv2.resize(img, None, fx = 0.5, fy = 0.5, interpolation = cv2.INTER_CUBIC)
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgray = cv2.GaussianBlur(imgray, (5,5), 0)
_,thresh = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('original', img)

_, contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

hull = []
for contour in contours:
    hull.append(cv2.convexHull(contour))

cv2.drawContours(img, hull, -1, (255, 120, 0), 4)

cv2.imshow('convex hull', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
