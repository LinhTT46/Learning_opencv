import cv2
import numpy as np 

x = np.uint8([250])
y = np.uint8([10])

print cv2.add(x, y)  # max = 255 --> 255

print x+y   # mod 256 -->4

