# import your necessary packages
import cv2
import imutils
import argparse

# construct an argparser and parse your arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", default="car.jpeg", help="Path to input image")
args = vars(ap.parse_args())

# load the image and display on it on the screen
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# grab the spatial dimentions of the image
(h, w) = image.shape[:2]

# NB Mainiting Aspect Ratio and when resizing images

# Let's resize our image to 150 pixels wide but in order to 
# prevent our image from being skewed/distorted, we must first
# calculate the ratio of the new width to the old width
r = 150.0 / w
dim = (150, int(h * r))

# perform the actual resize
resize = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("150w resized", resize)

# let's the resize the image with height 50pixels again keeping 
# the aspect ration
r = 50.0 / h
dim = (int(w * r), 50)

# perform the actual resize
resize = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("50 resized", resize)
cv2.waitKey(0)

# resizing with imutils
resize = imutils.resize(image=image, width=100)
cv2.imshow("imutils", resize)
cv2.waitKey(0)

# construct a list of interpolation methods in OPENCV
methods = [
    ("cv2.INTER_AREA", cv2.INTER_AREA),
    ("cv2.INTER_LINEAR", cv2.INTER_LINEAR),
    ("cv2.INTER_NEAREST", cv2.INTER_NEAREST),
    ("cv2.INTER_CUBIC", cv2.INTER_CUBIC),
    ("cv2.INTER_LANCZOS4", cv2.INTER_LANCZOS4)
]

# loop over the interpolation methods
for (name, method) in methods:
    # resize the width of the image 3x with the current interpolation method
    print(f"[INFO] {name}")
    
    resize = imutils.resize(image=image, width=w * 3, inter=method)
    
    cv2.imshow(f"{name}", resize)
    cv2.waitKey(0)