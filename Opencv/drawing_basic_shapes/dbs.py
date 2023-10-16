# import necessary packages we will need for the work
import numpy as np
import cv2
 
# create an empty canvas using the numpy array with 300 x 300
# with RGB channels
canvas = np.zeros((300,300, 3), dtype="uint8")

# let view the canvas using opencv
cv2.imshow("canvas", canvas)
cv2.waitKey(0)

# now lets draw a green line from the top-left corner 
# to the bottom right
green = (0, 255, 0)
cv2.line(canvas, (0, 0), (300,300), green)
cv2.imshow("canvas", canvas)
cv2.waitKey(0)

# now lets draw a red thick line from the top-right corner
# to the bottom left
red = (0, 0, 255)
cv2.line(canvas, (0, 300), (300, 0), red, 2)
cv2.imshow("canvas", canvas)
cv2.waitKey(0)

# let's draw a rectangle at the center of the screen with a 30 X 30 pixels 
# with a blue line 
blue = (255, 0, 0)
cv2.rectangle(canvas, ((300 // 2) - 30, (300 // 2) + 30), ((300 // 2) + 30, (300 // 2) - 30), blue)
cv2.imshow("canvas", canvas)
cv2.waitKey(0)

# let's draw a rectangle on the screen with a 50 X 50 pixels 
# with a blue fill color
blue = (255, 0, 0)
cv2.rectangle(canvas, (10, 10), (60, 60), blue, -1)
cv2.imshow("canvas", canvas)
cv2.waitKey(0)

# draw a white circle with a pixel size of 25
white = (255, 255, 255)
cv2.circle(canvas, (300//2, 300//2), 30, white)
cv2.imshow("canvas", canvas)
cv2.waitKey(0)