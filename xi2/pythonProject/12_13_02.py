import cv2
import numpy as np
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)
ret, img = cap.read()
kernel_Laplacian = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])

while True:
    ret, img = cap.read()
    cv2.imshow("Org", img)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Gray", gray)

    Laplacian1 = cv2.filter2D(gray, ddepth=cv2.CV_64F, kernel=kernel_Laplacian)
    abs_dst1 = cv2.convertScaleAbs(Laplacian1)
    cv2.imshow("Laplacian1", abs_dst1)

    Laplacian2 = cv2.Laplacian(gray, cv2.CV_64F)
    abs_dst2 = cv2.convertScaleAbs(Laplacian2)
    cv2.imshow("Laplacian2", abs_dst2)


    print(np.all(Laplacian2 == Laplacian1))

    if cv2.waitKey(1) & 0xFF is ord('q'):
        break

cap.release()
cv2.destroyAllWindows()