import cv2
import numpy as np


image = cv2.imread('./images/somi1.jpg')

cv2.imshow('ouput image origiinal', image)

#creating kernel
kernel = np.ones((5,5), np.uint8)

img_erosion = cv2.erode(image, kernel, iterations = 1)
img_dilation = cv2.dilate(image, kernel, iterations = 1)

cv2.imshow('image dilation', img_dilation)
cv2.imshow('image erosion', img_erosion)

cv2.waitKey(0)