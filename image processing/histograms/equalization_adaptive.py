import cv2
import numpy as np 

img = cv2.imread('equalization1.jpg', 0)

equa = cv2.equalizeHist(img)
res = np.hstack((img, equa))

clahe =  cv2.createCLAHE(clipLimit = 2.0, tileGridSize = (8,8))
cl1 = clahe.apply(img)


cv2.imshow('res', res)
cv2.imshow('cl1', cl1)
cv2.waitKey(0)
cv2.destroyAllWindows()
