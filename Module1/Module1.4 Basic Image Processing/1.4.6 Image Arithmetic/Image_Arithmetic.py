# import the necessary packages
import numpy as np
import argparse
import cv2
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())
# load the image and show it
image = cv2.imread(args["image"])
cv2.imshow("Original", image)
'''
Image arithmetic operations are simply no more than basic matrix addition and subtraction.
'''

# images are NumPy arrays, stored as unsigned 8 bit integers -- this
# implies that the values of our pixels will be in the range [0, 255]; when
# using functions like cv2.add and cv2.subtract, values will be clipped
# to this range, even if the added or subtracted values fall outside the
# range of [0, 255]. Check out an example:
print("max of 255: {}".format(str(cv2.add(np.uint8([200]), np.uint8([100])))))
print("min of 0: {}".format(str(cv2.subtract(np.uint8([50]), np.uint8([100])))))
# NOTE: if you use NumPy arithmetic operations on these arrays, the value
# will be modulo (wrap around) instead of being  clipped to the [0, 255]
# range. This is important to keep in mind when working with images.
print("wrap around: {}".format(str(np.uint8([200]) + np.uint8([100]))))
print("wrap around: {}".format(str(np.uint8([50]) - np.uint8([100]))))

