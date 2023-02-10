import cv2
import numpy as np

img = cv2.imread('./sample_noise.png', 0)
kernel = np.ones((5, 5), np.uint8)
print(kernel)

img_opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
cv2.imwrite('./sample_opening.png', img_opening)
