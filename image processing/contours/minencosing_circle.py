import cv2
import numpy as np 

img = cv2.imread('pen.png')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY)

_, contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    (x,y), radius = cv2.minEnclosingCircle(contour)
    center = (int(x), int(y))
    radius = int(radius)
    cv2.circle(img, center, radius,(0, 255, 255), 3)

cv2.imshow('enclosing circle', img)
cv2.waitKey(0)
cv2.destroyAllWindows()