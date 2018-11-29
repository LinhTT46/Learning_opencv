import cv2
import numpy as np 

img = cv2.imread('pen.png')
rows,cols = img.shape[:2]
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY)

_, contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    # fitting a ellipse
    # ellipse = cv2.fitEllipse(contour)
    # cv2.ellipse(img, ellipse.center, ellipse.axes, ellipse.angle, ellipse.startAngle,ellipse.endAngle,(255, 120, 0), 2)

    # fitting a line
    [vx,vy,x,y] = cv2.fitLine(contour, cv2.DIST_L2,0,0.01,0.01)
    lefty = int((-x*vy/vx) + y)
    righty = int(((cols-x)*vy/vx)+y)
    cv2.line(img,(cols-1,righty),(0,lefty),(0,255,0),2)

cv2.imshow('enclosing circle', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


