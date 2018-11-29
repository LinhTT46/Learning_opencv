import cv2
import numpy as np 

img = cv2.imread('messi.jpg', 0)
rows, cols = img.shape

p1 = np.float32([[50, 50], [50, 300], [300, 50], [300, 300]])
p2 = np.float32([[0,0], [0, 300], [300, 0], [300, 300]])

M = cv2.getPerspectiveTransform(p1, p2)
pert = cv2.warpPerspective(img, M, (cols, rows))

cv2.imshow('original', img)
cv2.imshow('perspective', pert)
cv2.waitKey(0)
cv2.destroyAllWindows()