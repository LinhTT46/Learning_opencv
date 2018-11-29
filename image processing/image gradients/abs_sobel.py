import cv2
import numpy as np 
from matplotlib import pyplot as plt 

img = cv2.imread('box.png', 0)

laplacian = cv2.Laplacian(img, cv2.CV_64F)
sobelx8u = cv2.Sobel(img, cv2.CV_8U, 1,0, ksize = 3)

sobelx64f = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize = 3)
abs_sobelx64f = np.absolute(sobelx64f)
sobel_8u = np.uint8(abs_sobelx64f)
plt.subplot(2,2,1),plt.imshow(img,cmap = 'gray')
plt.title('Original'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(laplacian,cmap = 'gray')
plt.title('Laplacian'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(sobelx8u,cmap = 'gray')
plt.title('Sobel CV_8U'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,4),plt.imshow(sobel_8u,cmap = 'gray')
plt.title('Sobel abs(CV_64F)'), plt.xticks([]), plt.yticks([])

plt.show()