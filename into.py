import sys
import numpy as n
import cv2


# main runnning code
img=cv2.imread('sample.jpg',0)
img = cv2.resize(img, (640, 640))
print(img)
cv2.imshow('img',img)
neg=255-img
print(neg)
cv2.imshow('neg',neg)
cv2.waitKey(0)
