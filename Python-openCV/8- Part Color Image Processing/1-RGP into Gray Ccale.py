import cv2
import matplotlib.pyplot as plt

#---------------Convert RGP image into Gray Ccale iamge---------------
image = cv2.imread("RGP.jpg")

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Displaying the original and the Converted
cv2.imshow("Input",  image)
cv2.imshow("Output", gray_image)
cv2.waitKey()
