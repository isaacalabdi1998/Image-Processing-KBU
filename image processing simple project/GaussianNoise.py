import cv2
import numpy as np

# Path Of Image
path = r"images/car.jpg"

# Send The Path To immread() Function
image = cv2.imread(path)

cv2.imshow("Original", image)

def gaussian_noise(image):
    row, col, ch = image.shape
    mean = 0
    var = 0.05
    sigma = var **0.5

    gauss = np.random.normal(mean, sigma, (row, col, ch))
    gauss = gauss.reshape(row, col, ch)
    noisy = image + gauss

    return noisy


image = cv2.imread(path)
image = image / 255
noise_img = gaussian_noise(image)

cv2.imshow("gaussian Noise", noise_img)
cv2.waitKey()