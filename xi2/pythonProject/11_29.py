import cv2
import numpy as np
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)  # capture image from web camera (ID=0)
ret, img = cap.read()  # capture image from web camera frame by frame
# 同画像処理はこのループ内で行いますが、今回はまだです。

kernel = np.array([
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]
])

kernel2 = np.array([
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
]) / 9

while True:
    ret, img = cap.read()  # capture image from web camera frame by frame
    cv2.imshow("Org", img)  # ?＿＿＿＿＿＿＿＿＿＿＿＿＿＿

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("My_gray_img", gray)

    sobel_img = cv2.filter2D(gray, -1, kernel)
    cv2.imshow("Sobel", sobel_img)

    avg_img = cv2.filter2D(gray, -1, kernel2)
    cv2.imshow("avg filter", avg_img)

    if cv2.waitKey(1) & 0xFF is ord('q'):  # press 'q' to finish
        break

cap.release()
cv2.destroyAllWindows()