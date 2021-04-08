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