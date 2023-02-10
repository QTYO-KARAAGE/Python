import time
import numpy as np
import cv2

t = time.localtime()
filename = str(t[0])+'_'+str(t[1])+'_'+str(t[2])+'_'+str(t[3])+'_'+str(t[4])+'_'+str(t[5])+'.bmp'
print(filename)

gray = cv2.imread("images\in\Lenna(gray)(10noize).bmp", 0)

h = gray.shape[0]
w = gray.shape[1]

output_img = gray.copy()
for h_start in range (w):
    for w_start in range (h):
        img = gray[h_start:h_start+3:1, w_start:w_start+3:1]
        output_img[h_start:h_start+3:1, w_start:w_start+3:1] = np.median(img)

print(output_img)
cv2.imshow("output_img_window", output_img)
cv2.imshow("img_window", gray)

k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('images/out/' + filename, gray)
    cv2.destroyAllWindows()
