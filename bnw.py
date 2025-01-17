import cv2
import numpy as np

img= cv2.imread('Me.jpg')
img = cv2.resize(img,(350, 500))
cv2.imshow('before',img)

image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

(thresh, bimage1) = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

(thresh, bimage2) = cv2.threshold(image, 150, 200, cv2.THRESH_BINARY)
cv2.imshow('BnW_image_with_1st_threshold_value',bimage1)
cv2.waitKey(0) 
cv2.imshow('BnW_image_with_2nd_value',bimage2)
cv2.waitKey(0) 
cv2.destroyAllWindows()