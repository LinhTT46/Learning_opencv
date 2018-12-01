import cv2
import numpy as np 
import matplotlib.pyplot as plt 

img = cv2.imread('equalization.png', 0)
hist, bins = np.histogram(img.flatten(), 255, [0, 256])

cdf = hist.cumsum()
cdf_m = np.ma.masked_equal(cdf,0)
cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())
cdf = np.ma.filled(cdf_m,0).astype('uint8')

img2 = cdf[img]
plt.subplot(121), plt.imshow(img2, 'gray')
plt.title('cdf'), plt.xticks([]), plt.yticks([])

plt.subplot(122)
plt.plot(cdf, color = 'r')
plt.hist(img2.flatten(), 256, [0,256], color = 'b')
plt.xlim([0,256])
plt.legend(('cdf', 'histogram'), loc = 'upper left')
plt.show()