# import all the necessary packages
import cv2
import argparse

# construct an argparser to parse the arguements
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", default="car.jpeg", type=str, help="path to input image")
args = vars(ap.parse_args())

# load the image and display it on the screen
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# here we split the image to various channels 
(B, G, R) = cv2.split(image)

# we show all the various channels in the screen
cv2.imshow("Blue", B)
cv2.imshow("Green", G)
cv2.imshow("Red", R)
cv2.waitKey(0)

# merge the image back together
merge = cv2.merge([B, G, R])
cv2.imshow("Merge", merge)
cv2.waitKey(0)
cv2.destroyAllWindows()