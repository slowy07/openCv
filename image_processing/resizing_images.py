import cv2 
import numpy as np  
import matplotlib.pyplot as plt

image = cv2.imread('./images/somi.jpg')
half = cv2.resize(image, (0,0), fx = 0.1, fy = 0.1)
bigger = cv2.resize(image, (1050, 1610))

strech_near = cv2.resize(image, (780,540), interpolation = cv2.INTER_NEAREST)

titles = ['original', 'half', 'bigger', 'interpolation nearest']
images = [image, half, bigger, strech_near]
count = 4
for i in range(count):
    plt.subplot(2, 2, i+1)
    plt.title(titles[i])
    plt.imshow(images[i])

plt.show()