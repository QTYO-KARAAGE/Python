import cv2
import numpy as np

img = cv2.imread('./sample.png', 0)
kernel = np.ones((5, 5), np.uint8)
img_erode = cv2.erode(img, kernel, iterations=1)

cv2.imwrite('./sample_erode.png', img_erode)

print(kernel)
