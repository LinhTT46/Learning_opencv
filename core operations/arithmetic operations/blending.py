import cv2 
import numpy as np 

# same size
img1 = cv2.imread('la.png')
img2 = cv2.imread('lal.png')

dst = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)

cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

