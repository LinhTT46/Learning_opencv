import cv2
import numpy as np  

img = cv2.imread('equalization.png', 0)

# input: gray image,  output: histogram equalized image.
equa = cv2.equalizeHist(img)

# staking image side by side.
res = np.hstack((img, equa))

cv2.imshow('res', res)
cv2.waitKey(0)
cv2.destroyAllWindows()