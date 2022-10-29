import numpy as np
import cv2


foto = cv2.imread("prag.jpg",0)
cv2.imshow("...",foto)
cv2.waitKey()

[w,h] = foto.shape
u=0
f_max=0
for v in range (0,h):
    for u in range (0,w):
        f_max+=foto[u,v] #np.max(foto)
print(f_max)
v,u=0,0
for v in range (0, h):
    for u in range (0,w):
        foto[u,v]=255-foto[u,v]
        if foto[u,v]<0:
            foto[u,v]=0
cv2.imshow("...",foto)
cv2.waitKey()
