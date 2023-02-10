import time
import numpy as np
import cv2

t = time.localtime()
filename = str(t[0])+"_"+str(t[1])+"_"+str(t[2])+"_"+str(t[3])+"_"+str(t[4])+"_"+str(t[5])+".bmp"
print(filename)

gray = cv2.imread("images\in\Lenna(gray)(10noize).bmp", 0)

 

H = gray.shape[0]
W = gray.shape[1]
output_img = gray.copy()
kh = 3
kw = 3
for h in range(H):
    for w in range(W):
        img= gray [h:h + kh:1,     w:w + kw:1]
        output_img[h:h + kh:1,     w:w + kw:1]=np.median(img)

 

print(output_img)
cv2.imshow("org_img_window",gray)
cv2.imshow("output_img_window",output_img)

 

k = cv2.waitKey(0)
if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite("images/out/" + filename, gray)
    cv2.destroyAllWindows()