import cv2
import numpy as np 

img = cv2.imread('pen.png')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
mask = np.zeros(imgray.shape, np.uint8)
_, thresh = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY)

_, contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    area = cv2.contourArea(contour)
    rect_area = w * h 
    hull = cv2.convexHull(contour)
    hull_area = cv2.contourArea(hull)
    aspect_ratio = float(w)/h  # aspect_ratio = width / height
    extend = float(area) / rect_area # extend = area(contour) / area(rect)
    solidity = float(area) / hull_area # solidity = area(contour)/ area(hull)
    equi_diameter = np.sqrt(4 * area/np.pi) # equi_diameter
    
    # #(x,y), (MA, ma), angle = cv2.fitEllipse(contour)
    # cv2.drawContours(mask, [contour], 0, (255,0,0), -1)
    # pixelpoints = np.transpose(np.nonzero(mask))

    # Extreme points
    leftmost = tuple(contour[contour[:,:,0].argmin()] [0])
    rightmost = tuple(contour[contour[:,:,0].argmax()] [0])
    topmost = tuple(contour[contour[:,:,1].argmin()] [0])
    bottommost = tuple(contour[contour[:,:,1].argmax()] [0])
    cv2.circle(img, leftmost, 8, (255,127,0), -1)
    cv2.circle(img, rightmost, 8, (255,127,0), -1)
    cv2.circle(img, topmost, 8, (255,127,0), -1)
    cv2.circle(img, bottommost, 8, (255,127,0), -1)



#  Maximum Value, Minimum Value and their locations
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(imgray, mask = mask)
cv2.circle(img, min_loc, 9, (0,255,255), -1)
cv2.circle(img, max_loc, 9, (0,255,255), -1)

# Mean Color (Mean Intensity)
min_valc = cv2.mean(img, mask = mask)
  

cv2.imshow('original', img)
cv2.waitKey(0)
cv2.destroyAllWindows()