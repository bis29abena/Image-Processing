# import your necessary packages
import cv2 
import argparse

# construct your argpraser to parse your arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", default="car.jpeg", type=str, help="path to input image")
args = vars(ap.parse_args())

# load the input image and show it on the screen
image = cv2.imread(args["image"])
cv2.imshow("Car", image)

# we crop the image using numpy array slicing
# array slices in startY:endY, startX:endX
# here we crop the body of the from the whole image
car_body = image[63:181, 36:214]
cv2.imshow("car_body", car_body)
cv2.waitKey(0)


# apply another image cropping to exctract only the tyre of the car
car_tyre = image[111:144, 116:147]
cv2.imshow("car_tyre", car_tyre)
cv2.waitKey(0)