import os
os.environ["OPENCV_VIDEO_IO_MSNF_ENABLE_HW_TRANSFORMS"] = '0'

import cv2
cap = cv2.VideoCapture(0)

import numpy as np

n = 1
while True:
    ret, img = cap.read()
    cv2.imshow("org", img)

    if cv2.waitKey(1) & 0xFF is ord('a'):
        n = n + 1

    if cv2.waitKey(1) & 0xFF is ord('z'):
        n = n - 1

    if cv2.waitKey(1) & 0xFF is ord('q'):
        break

    print('n = ', n)

    img_rotate = np.rot90(img, n)
    h = img.shape[0]
    w = img.shape[1]
    rotate_matrix = cv2.getRotationMatrix2D(center=(w/2, h/2), angle=45, scale=1)
    rotated_image = cv2.warpAffine(src=img, M=rotate_matrix, dsize=(w, h))
    cv2.imshow("rotated_image", rotated_image)

    tx = 100
    ty = 100
    mv_mat = np.float32([
        [1, 0, tx],
        [0, 1, ty]
    ])
    moved_image = cv2.warpAffine(src=img, M=mv_mat, dsize=(w, h))
    cv2.imshow('moved_image', moved_image)

cap.release()
cv2.destroyAllWindows()
