import cv2
import numpy as np 
import matplotlib.pyplot as plt

img = cv2.imread('appro.png')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('original', img)

_, contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

approx001 = [] # approximation for epsilon = 0.01% of the arc length
approx01 = []  # approximation for epsilon = 0.1% of the arc length
for contour in contours:
    # epsilon = 0.01% of the arc length
    epsi001 = 0.01 * cv2.arcLength(contour, True)
    app001 = cv2.approxPolyDP(contour, epsi001, True)
    approx001.append(app001)

    # epsilon = 0.1% of the arc length
    epsi01 = 0.1 * cv2.arcLength(contour, True)
    app01 = cv2.approxPolyDP(contour, epsi01, True)
    approx01.append(app01)
    

# draw blue color for epsilon = 0.01% of the arc length
cv2.drawContours(img, approx001, -1, (255, 120, 0), 5)

# draw red color for epsilon = 0.1% of the arc length
cv2.drawContours(img, approx01, -1, (0, 0, 255), 2)


cv2.imshow('approximation', img)
cv2.waitKey(0)
cv2.destroyAllWindows()



