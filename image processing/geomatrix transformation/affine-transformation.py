import cv2
from matplotlib import pyplot as plt
import numpy as np 

img = cv2.imread('rectangle.jpg')
rows, cols = img.shape[:2]

pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[0,100],[200,50],[100,250]])
M = cv2.getAffineTransform(pts1, pts2)

aft = cv2.warpAffine(img, M, (cols,rows))

# 1. show by matplotlib
plt.subplot(121), plt.imshow(img), plt.title('Input')
plt.subplot(122), plt.imshow(aft), plt.title('Output')
plt.xticks([]), plt.yticks([])
plt.show()


# 2. show by cv2
# cv2.imshow('original', img)
# cv2.imshow('afftrans', aft)
# cv2.waitKey(0)
# cv2.destroyAllWindows()