import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, img = cap.read()
    cv2.imshow("Org", img)

    #create noise image
    print(img.shape, img.shape[0], img.shape[1])

    gauss_noise = np.zeros((img.shape[0], img.shape[1]), dtype = np.uint8)
    cv2.randn(gauss_noise, 128, 20)
    gauss_noise = (gauss_noise * 0.5).astype(np.uint8)
    cv2.imshow("gauss_noise", gauss_noise)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gauss_noise_img = cv2.add(gray, gauss_noise)
    cv2.imshow("gauss_noise_img", gauss_noise_img)

    bilateral = cv2.bilateralFilter(gauss_noise_img, 15, 20, 20)
    cv2.imshow("bilateral", bilateral)

    average_filter = cv2.blur(gauss_noise_img, (5, 5))
    cv2.imshow("average_filter", average_filter)

    if cv2.waitKey(1) & 0xFF is ord("q"):
        break


cap.release()
cv2.destroyAllWindows()