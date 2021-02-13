import cv2
import numpy

image = cv2.imread('./images/somi1.jpg')
background_subtract = cv2.createBackgroundSubtractorMOG2()

result = background_subtract.apply(image)

cv2.imshow('output', result)

if cv2.waitKey(0) & 0xFF == 27:
    cv2.destroyAllWindows()

"""
video = cv2.VideoCapture('./video/people_walking_in_city.mp4')
while(1):
    ret, frame = video.read()
    result_masking = background_subtract.apply(frame)

    cv2.imshow('output', result_masking)

    if cv2.waitKey(0) & 0xFF == 27:
        break

video.release()
cv2.destroyAllWindows()
"""