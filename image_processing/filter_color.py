import cv2
import numpy as np


image = cv2.imread('./images/somi.jpg')

image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lower_blue = np.array([25, 140, 60])
upper_blue = np.array([255, 235, 180])

masking = cv2.inRange(image_hsv, lower_blue, upper_blue)
result = cv2.bitwise_and(image, image, mask = masking)

cv2.imshow('result', result)
cv2.imshow('mask', masking)
cv2.imshow('original', image)
if cv2.waitKey(0) & 0xFF == 27:
    cv2.destroyAllWindows()