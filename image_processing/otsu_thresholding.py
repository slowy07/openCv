import cv2
import numpy as np

image = cv2.imread('./images/somi1.jpg')

#convert image to grayscale
image_grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


ret, thresh1 = cv2.threshold(image_grayscale, 120, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imshow('image with otsu thesholding', thresh1)

if cv2.waitKey(0) & 0xFF == 27:
    cv2.destroyAllWindows()