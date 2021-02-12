import cv2

image = cv2.imread('./images/somi1.jpg')

grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
rgba_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGBA)

cv2.imshow('grayscale image', grayscale_image)
cv2.imshow('hsv image', hsv_image)
cv2.imshow('rgba image', rgba_image)

if cv2.waitKey(0) & 0xFF == 27:
    cv2.destroyAllWindows()