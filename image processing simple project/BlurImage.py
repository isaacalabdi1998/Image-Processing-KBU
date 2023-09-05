import cv2
import numpy as np

#Read The Image
image = cv2.imread("images/car.jpg")

# Craeting The Kernal (2D Convolution Matrix)
kernall = np.ones((5, 5), np.float32) / 30

# Applying The Fillter2D Function
img = cv2.filter2D(src=image, ddepth=-1, kernel=kernall)

# Showing The Orignal And Output Image
cv2.imshow("Orignal", image)
cv2.imshow("kernall", img)

cv2.waitKey()