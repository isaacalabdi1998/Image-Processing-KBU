import cv2
import numpy as np
import matplotlib.pyplot as plt

row = 256
col = 256

image = np.zeros((row, col))
image[100 : 105, : ] = 0.5
image[ :, 100:105] = 1

plt.figure(figsize=(10, 4))
plt.imshow(image)
plt.show()

cv2.waitKey()