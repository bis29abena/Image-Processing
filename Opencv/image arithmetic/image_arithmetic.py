# import the necessary packages
import cv2
import argparse
import numpy as np

# construct an argument parser to parse an argument
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", default="tree.jpeg", type=str, help="path to input image")
args = vars(ap.parse_args())

# load the image and display
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# images are Numpy Arrays stores as unsigned 8-bit integers(uint8)
# with values in the range [0, 255]; when using add/subtract
# functions in OpenCv, the values will be *clipped* to this range,
# even if they fall outside the range [0, 255] after applying the
# operation
added = cv2.add(np.uint8([200]), np.uint8([100]))
subtract = cv2.subtract(np.uint8([50]), np.uint8([100]))
print(f"max of 255: {added}")
print(f"min of 0: {subtract}")

# increasing the pixel intensity of our image by 100
# is accomplished by constructing a numpy array that has the 
# same dimension as our input image, filling it with ones 
# multiplying by 100, and then adding the input image and matrix together
M = np.ones(image.shape, dtype="uint8") * 100
added = cv2.add(image,M)
cv2.imshow("Brightened image", added)

# when we want to darken the input image 
# we follow the same process
M = np.ones(image.shape, dtype="uint8") * 50
subtract = cv2.subtract(image, M)
cv2.imshow("Darkened Image", subtract)
cv2.waitKey(0)

