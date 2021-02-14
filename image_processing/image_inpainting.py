import cv2

image = cv2.imread('./images/somi.jpg')

#mask load
mask_image = cv2.imread('./images/somi.jpg', 0)

inpaint_image = cv2.inpaint(image, mask_image ,2, cv2.INPAINT_NS)

cv2.imshow('result', inpaint_image)

"""
save image
cv2.imwrite('result_inpainted', inpaint_image)
"""
if cv2.waitKey(0) & 0xFF == 27:
    cv2.destroyAllWindows()