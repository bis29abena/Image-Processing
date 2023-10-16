import argparse
import cv2

# creating your argument parser to get the image from a specified path
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to your image")
args = vars(ap.parse_args())

# using open cv to read the image into memory
image = cv2.imread(args["image"])
# grabbing the spatial dimension of the image
(h, w) = image.shape[:2]
# showing the image on screen
cv2.imshow("car image", image)
# printing the image height and width on screen
print(f"The height of the image is {h} and the wdith is {w}")

# getting the color ordering from a specific pixel
# thats the top left corner the image
# and showing it on the screen
(b, g, r) = image[0, 0]
print(f"Pixel at (0, 0) for Red: {r}, Green: {g}, Blue: {b}")

# accessing the pixel intensities at position x=50, y=20
(b, g, r) = image[20, 50]
print(f"Pixel at (50, 20) for Red: {r}, Green: {g}, Blue: {b}")

# updating the pixel intensity at position x=50, y=20 to a blue color 
# and after printing it on the screen
image[20, 50] = (255, 0, 0)
(b, g, r) = image[20, 50]
print(f"Pixel Update at (50, 20) for Red: {r}, Green: {g}, Blue: {b}")

# grab the center of the image
# that's dividing the width and height by 2
(ch, cw) = (h//2, w//2)

# since we are using Numpy arrays we can apply array slicing 
# to extract large chunks/region of interest from the image
# here we grab the top left corner of the image and display on the screen
tl_corner = image[0:ch, 0:cw]
# print(image[0:ch, 0:cw])
cv2.imshow("top_left", tl_corner)

# in similar fashion we can get the top-right, bottom-left,
# and bottom right of the image and display it on the screen
# this is the technique used for image cropping
tr_corner = image[0:ch, cw:w]
bl_corner = image[ch:h, 0:cw]
br_corner = image[ch:h, cw:w]

cv2.imshow("top_right", tr_corner)
cv2.imshow("bottom_left", bl_corner)
cv2.imshow("bottom_right", br_corner)

# updating the top-left of the image to a blue color
image[0:ch, 0:cw] = (255, 0, 0)
cv2.imshow("uodate_topLeft", image)

cv2.waitKey(0)
