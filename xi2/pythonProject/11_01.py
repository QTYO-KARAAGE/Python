import numpy as np

img = np.zeros((3, 3))

img[0:1:1 , ] = 200, 150, 200
img[1:2:1 , ] = 15, 3, 100
img[2:3:1 , ] = 20, 0, 4
print(img)
print('median=', np.median(img))