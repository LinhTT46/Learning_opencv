import cv2 
import numpy as np 

# create a black image
img = np.zeros((512, 512, 3), np.uint8)

# draw a diagonal blue line
cv2.line(img, (0,0), (511, 511), (255), 5)

# draw a rectangle at the top-right corner
cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)

# draw a circle inside rectangle drawn above
cv2.circle(img, (447, 63), 63, (0, 0, 255), -1) # thickness = -1 for fill

# draw ellipse
cv2.ellipse(img, (256, 256), (100, 50), 0, 45, 360, 255, -1)

# draw polygon  = draw multiple lines(faster than cv2.line)
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv2.polylines(img, [pts], False, (0, 255, 255), 4) # True for closed shape

# adding text
font = cv2.FONT_HERSHEY_PLAIN
cv2.putText(img, 'La La La', (10, 500), font, 5, (120, 120, 0), 2, cv2.LINE_AA)

cv2.imshow('drawing', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
