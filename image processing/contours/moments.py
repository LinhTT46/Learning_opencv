import cv2
import numpy as np 

img = cv2.imread('squares.png')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 155, 255, 0)
cv2.imshow('original', img)

_, contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

for contour in contours:
    area = cv2.contourArea(contour)
    perimeter = cv2.arcLength(contour, True)
    
    if area > 500: 
        cv2.drawContours(img, contour, -1, (0, 0, 255), 3)
        print cv2.moments(contour)
    if perimeter > 50:
        cv2.drawContours(img, contour, 3, (255,100, 0), 8)
        print perimeter
    
print 'Length: ' ,len(contours)
cv2.imshow('draw',img)
cv2.waitKey(0)
cv2.destroyAllWindows()