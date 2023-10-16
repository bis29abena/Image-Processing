# import the necessary packages
import cv2
import argparse

# construct an argument parser and parse your arguments
ap = argparse.ArgumentParser()

ap.add_argument("-i", "--image", default="car.jpeg", help="path to inout image", type=str)
args = vars(ap.parse_args())

# read the image and show it on screen
image = cv2.imread(args["image"])
cv2.imshow("Car", image)

# flip the image horizontally
# and show it on the screen
flip_image = cv2.flip(image, 1)
cv2.imshow("Horizontal", flip_image)

# flip the image vertically
flip_image = cv2.flip(image, 0)
cv2.imshow("Vertical", flip_image)

# flip the image both horizontal and vertical
flip_image = cv2.flip(image, -1)
cv2.imshow("Both", flip_image)

cv2.waitKey(0)