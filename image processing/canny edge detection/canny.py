import cv2
import numpy as np

img = cv2.imread('messi.jpg',0)
edges = cv2.Canny(img, 120, 150)

cv2.imshow('original', img)
cv2.imshow('canny', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()