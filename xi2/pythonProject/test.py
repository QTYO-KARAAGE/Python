import matplotlib.pyplot as plt
import numpy as np

#plot (x,y) pairs ; from (2, 3) to (7, 5),
xpoints = np.array([2, 7]) #The x-axis is the horizontal axis.
ypoints = np.array([3, 5])# The y-axis is the vertical axis.
plt.plot(xpoints, ypoints)
plt.show()
