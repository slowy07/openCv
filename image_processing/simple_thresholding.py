import cv2
import numpy as np

image = cv2.imread('./images/somi1.jpg')
#conver image to grayscale
grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


"""
applyin different thresholding 
into image
all pixel value above 120 will
bee set into 255
"""

ret, thresholding1 = cv2.threshold(grayscale_image, 120, 255, cv2.THRESH_BINARY)
ret, thresholding2 = cv2.threshold(grayscale_image, 120, 255, cv2.THRESH_BINARY_INV)
ret, thresholding3 = cv2.threshold(grayscale_image, 120, 255, cv2.THRESH_TRUNC)
ret, thresholding4 = cv2.threshold(grayscale_image, 120, 255, cv2.THRESH_TOZERO)
ret, thresholding5 = cv2.threshold(grayscale_image, 120, 255, cv2.THRESH_TOZERO_INV)

cv2.imshow('binary threshold', thresholding1)
cv2.imshow('binary threshold inverted', thresholding2)
cv2.imshow('truncated threshold', thresholding3)
cv2.imshow('set to 0', thresholding4)
cv2.imshow('set to 0 inverted', thresholding5)




if cv2.waitKey(0) & 0xFF == 27:
    cv2.destroyAllWindows()