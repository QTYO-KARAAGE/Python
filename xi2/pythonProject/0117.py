import cv2
import numpy as np

cap = cv2.VideoCapture(0)
size = 0

while True:
    ret, img = cap.read()
    w = 800 + size
    h = 600 + size
    cv2.imshow('Org', img)

    resized = cv2.resize(img, (w, h))
    cv2.imshow('resized_img', resized)
    print(img.size, '--->', resized.shape)

    #  'A'で+10づつの拡大
    if cv2.waitKey(1) & 0xFF is ord('a'):
        size = size + 10

    #  'Z'で-10づつの縮小
    if cv2.waitKey(1) & 0xFF is ord('z'):
        size = size - 10

    if cv2.waitKey(1) & 0xFF is ord('q'):
        break

    print(size)

cap.release()
cv2.destroyAllWindows()
