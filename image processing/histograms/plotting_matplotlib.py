import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('plotting_home.png',0)
img1 = cv2.imread('plotting_home.png')


# histogram for gray image directly
plt.hist(img.ravel(), 256, [0, 256])
plt.show()

# for BGR plot
color =('b', 'g', 'r')
for i, col in enumerate(color):
    histr = cv2.calcHist([img1], [i], None, [256], [0,256])
    plt.plot(histr, color = col)
    plt.xlim([0,256])

plt.show()
