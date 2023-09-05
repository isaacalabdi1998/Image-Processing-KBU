import cv2
import numpy as np

# Path Of Image
path = r"images/car.jpg"

# Send The Path To immread() Function
img = cv2.imread(path)

image1 = cv2.blur(img, (5, 5))
image2 = cv2.boxFilter(img, -1, (2, 2), normalize=True)

# Showwing The Output
cv2.imshow("Image", np.hstack((image1, image2)))

cv2.waitKey()
cv2.destroyAllWindows()