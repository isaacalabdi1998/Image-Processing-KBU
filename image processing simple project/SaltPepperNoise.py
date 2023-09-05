import random
import cv2

def add_noise(img): 
    row, col = img.shape
    number_of_pixels = random.randint(300, 10000)

    for index in  range(number_of_pixels):
        y_coord = random.randint(0, row -1)
        x_coord = random.randint(0, col -1)
        img[y_coord][x_coord] = 255

    number_of_pixels = random.randint(300, 10000)
    for index in range(number_of_pixels):
        y_coord = random.randint(0, row -1)
        x_coord = random.randint(0, col -1)
        img[y_coord][x_coord] = 0
    

    return img


# Path Of Image
path = r"images/car.jpg"

# Send The Path To immread() Function
image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
cv2.imwrite("Output.jpg", add_noise(image))

cv2.waitKey()