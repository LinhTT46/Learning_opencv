import cv2
import numpy as np 

img = cv2.imread('messi.jpg')
rows, cols = img.shape[:2]

M = cv2.getRotationMatrix2D((cols/2, rows/2), 90, 1)
rot = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow('original', img)
cv2.namedWindow('rotation', cv2.WINDOW_NORMAL)
cv2.imshow('rotation', rot)
cv2.waitKey(0)
cv2.destroyAllWindows()
