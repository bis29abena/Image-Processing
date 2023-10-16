# import the necessary packages
import cv2
import numpy as np
import argparse

# construct an argument parser to parse your arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", default="car.jpeg", type=str, help="path to input image")
args = vars(ap.parse_args())

# load the image and display it on the screen
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# construct the mask for your image
# a mask is the same size of your image but only has two pixel
# value that's 0 or 255
mask = np.zeros(image.shape[:2], dtype="uint8")
cv2.rectangle(mask, (30, 67), (220, 150), 255, -1)
cv2.imshow("mask", mask)

# apply our mask
masked = cv2.bitwise_and(image, image, mask=mask)
cv2.imshow("masked", masked)

cv2.waitKey(0)