import cv2

image = cv2.imread('./images/somi.jpg')

bilateral = cv2.bilateralFilter(image, 15,75,75)

cv2.imshow('original', image)
cv2.imshow('ouput', bilateral)

if cv2.waitKey(0) & 0xFF == 27:
    cv2.destroyAllWindows()