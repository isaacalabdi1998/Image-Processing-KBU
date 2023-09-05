
import cv2
import numpy as np

# Path Of Image
path = r"images/Brain.jpg"

# Send The Path To immread() Function
image = cv2.imread(path)

# Applying medianBlur() Function
median = cv2.medianBlur(image, 5)

# Applying medianBlur() concatenate
compare = np.concatenate((image, median), axis=1)

# Side By Side Comparison
cv2.imshow("Image", compare)


cv2.waitKey()