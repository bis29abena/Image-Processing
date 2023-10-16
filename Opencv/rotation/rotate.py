# import the necessary packages
import cv2
import imutils
import argparse

# construct and argument parser and parse your arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", default="car.jpeg", help="path to the input image")
arg = vars(ap.parse_args())

# load the image and show it
image = cv2.imread(arg["image"])
cv2.imshow("Car Image", image)

# grap the spatial dimensions of the image and calculate
# the center of the image
(h, w) = image.shape[:2]
(ch, cw) = (h // 2, w // 2)

# NB postive values rotate your image anticlock wise and 
#    negative values totate your image clock wise

# rotate your image about 45 degrees around the center of your image
M = cv2.getRotationMatrix2D((cw, ch), 45, 1.0)
rotate = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated 45 degrees anti clock wise", rotate)

# rotate your image -90 degrees around the center of your image
M = cv2.getRotationMatrix2D((cw, ch), -90, 1.0)
rotate = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated 90 degrees clock wise", rotate)

# rotate your image around an arbitrary point rather than the center
M = cv2.getRotationMatrix2D((10, 10), -33, 1.0)
rotate = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated at any point", rotate)

# using the imutils rotate function for rotation
rotate = imutils.rotate(image, 180)
cv2.imshow("Imutils Rotate", rotate)

# use rotate_bound to fit the image in the area view
rotate = imutils.rotate_bound(image=image, angle=-33)
cv2.imshow("Rotate Bound", rotate)
cv2.waitKey(0)