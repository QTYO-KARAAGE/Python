import cv2
import numpy as np
import matplotlib.pyplot as plt

a = np.array([4, 4, 4])
b = np.array([4, 3, 4])
print(np.all(a == b))

a = np.array([[3, 3, 3], [3, 3, 3]])
b = np.array([[3, 3, 3], [3, 3, 4]])
print(np.all(a == b))

exit()