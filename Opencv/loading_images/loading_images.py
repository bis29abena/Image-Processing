import argparse
import cv2

ap = argparse.ArgumentParser()

ap.add_argument("-i", "--image", required=True, help="Path to your input image")
arg = vars(ap.parse_args())

image = cv2.imread(arg["image"])

(h, w, c) = image.shape

print(f"The height of the image is {h}")
print(f"The width of the image is {w}")
print(f"The channels of the image is {c}")

cv2.imshow("image", image)
cv2.waitKey(0)
