import cv2
import numpy as np 
import matplotlib.pyplot as plt 

img = cv2.imread('equalization.png', 0)

hist, bins = np.histogram(img.flatten(), 256, [0,256])

cdf = hist.cumsum()
cdf_normalized = cdf * float(hist.max()) /cdf.max()

plt.subplot(121), plt.imshow(img, 'gray')
plt.title('original'), plt.xticks([]), plt.yticks([])
plt.subplot(122)
plt.plot(cdf_normalized, color = 'b')
plt.hist(img.flatten(),256,[0,256], color = 'r')
plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()

