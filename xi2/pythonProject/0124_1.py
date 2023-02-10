import cv2
import numpy as np

img = cv2.imread('./sample.png', 0)
kernel = np.ones((5, 5), np.uint8)
print(kernel)

img_dilate = cv2.dilate(img, kernel, iterations=1)
cv2.imwrite('sample_dilate.png', img_dilate)
