import cv2
import numpy as np 
import matplotlib.pyplot as plt 

img = cv2.imread('paper.jpg', 0)
img = cv2.GaussianBlur(img, (5,5), 0)

ret,th1 = cv2.threshold(img,145,255,cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY,75,2)
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,75,2)

titles = ['Blur', 'Global Thres(t = 145)', 'Adaptive MeThres',
         'Adaptive GsThres']
images = [img, th1, th2, th3]

for i in range (4):
    plt.subplot(2, 2, i+1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()