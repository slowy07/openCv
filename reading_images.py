import cv2

img = cv2.imread('images/somi.jpg', cv2.IMREAD_COLOR)

#cv2.imshow('output image', img)

#opening grayscale mode
path = r'images/somi.jpg'
grayImage  = cv2.imread(path, 0)

cv2.imshow('grayscale image', grayImage)

cv2.waitKey(0)
cv2.destroyAllWindows()