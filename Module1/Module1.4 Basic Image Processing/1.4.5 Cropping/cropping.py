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

'''
As the name suggests, cropping is the act of 
selecting and extracting the Region of Interest (or simply, ROI), which is the part of the image we are interested in.
When we crop an image, we want to remove the outer parts of the image that we are not interested in. This is commonly called selecting our Region of Interest, or more simply, our ROI.

'''
#Lets crop a region  from the image
cropped_region = image[4 :1500,40:800]
#Show the cropped region
cv2.imshow("Cropped Region",cropped_region)
cv2.waitKey(0)
cv2.destroyAllWindows()


