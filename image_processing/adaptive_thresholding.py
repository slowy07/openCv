import cv2
import numpy as np


image = cv2.imread('./images/somi.jpg')

#convert image to grayscale
grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


#get diferrent thresholding
thresh1 = cv2.adaptiveThreshold(grayscale_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 199, 5)
thresh2 = cv2.adaptiveThreshold(grayscale_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 199, 5)

cv2.imshow('adaptive mean', thresh1)
cv2.imshow('adaptive gaussian', thresh2)

if cv2.waitKey(0) & 0xFF == 27:
    cv2.destroyAllWindows()