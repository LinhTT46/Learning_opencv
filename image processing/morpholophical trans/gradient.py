import cv2
import numpy as np 

img = cv2.imread('j.png', 0)
kernel = np.ones((5,5), np.uint8)

# gradient = dilation - erosion
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

cv2.imshow('original', img)
cv2.imshow('gradient', gradient)
cv2.waitKey(0)
cv2.destroyAllWindows()