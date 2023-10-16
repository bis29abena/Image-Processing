# import your necessary packages
import numpy as np
import cv2
import argparse
import imutils

# initialize your argparse and add your arguments
# you want your code to be accepting
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", default="car.jpeg", type=str, help="path to your input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Car", image)

(h, w) = image.shape[:2]

# shift the image 25 pixels to the right and 50 pixels down
M = np.float32([[1, 0, 25], [0, 1, 50]])
shifted_image_right = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Shifted image right", shifted_image_right)

# now let's shift the image 50 pixels to the left and 90 pixels downwards
# by giving the xy cordinates negative values respectively
M = np.float32([[1, 0, -50], [0, 1, -90]])
shifted_image_left = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Shifted image left", shifted_image_left)

shifted_image_imutils = imutils.translate(image, 0, 100)
cv2.imshow("Shifted image imutils", shifted_image_imutils)
cv2.waitKey(0)