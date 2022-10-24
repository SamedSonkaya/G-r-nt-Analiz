import numpy as np
import cv2
from matplotlib import pyplot as plt
from numpy import zeros

foto = cv2.imread("prag.jpg")
cv2.imshow("...",foto)
cv2.waitKey()

B=foto[:,:,0]
G=foto[:,:,1]
R=foto[:,:,2]

imgGray = 0.2989 * R + 0.5870 * G + 0.1140 * B
plt.imshow(imgGray, cmap='gray')
plt.show()

imgGray =cv2.imread("prag.jpg",0)
plt.hist(imgGray)
plt.show()

i,u=0,0
Hist = zeros(256)
[w,h] = imgGray.shape
for v in range (0, u<h):
    for u in range (0, u<w):
        i= imgGray[u,v]
        Hist[i]=Hist[i]+1
plt.hist(Hist)
plt.show()



