import cv2
import numpy as np

image = cv2.imread('./images/somi.jpg')
window_name = 'Image'

#creating kernels
kernel = np.ones((5,5), np.uint8)
#using cv2.erode()
eroding_images = cv2.erode(image, kernel)
cv2.waitKey(0)
cv2.imshow(window_name, eroding_images)
