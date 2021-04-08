import cv2
import argparse
import numpy as np
import imutils
ap= argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Path of the image")
args =vars(ap.parse_args())


#load the image
image =cv2.imread(args['image'])
cv2.imshow("Original Image",image)

'''Similar to rotation, OPENCV provides a method to flip the image across its x or y axis.
'''

#Flip the image horizontally
flipped = cv2.flip(image,1)
cv2.imshow(" Flipped Horizontally",flipped)

#Flip the image vertically
flip_vertical = cv2.flip(image,0)
cv2.imshow("Flipped Vertically",flip_vertical)

# flip the image along both axes
flipped = cv2.flip(image, -1)
cv2.imshow("Flipped Horizontally & Vertically", flipped)
cv2.waitKey(0)

