import cv2
import numpy as np

image = cv2.imread('./images/somi.jpg')

gaussian_image = cv2.GaussianBlur(image, (7, 7), 0)
cv2.imshow('otiginal image', image)
cv2.imshow('gaussian blur image', gaussian_image)
cv2.waitKey(0)
cv2.destroyAllWindows()