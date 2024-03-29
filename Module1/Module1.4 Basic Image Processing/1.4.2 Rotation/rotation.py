#Import all the required files
import cv2
import numpy as np
import imutils
import argparse
ap= argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Path of the image")
args =vars(ap.parse_args())

#Load the image
image = cv2.imread(args['image'])
#Display the original image
cv2.imshow("Original Image",image)

'''Rotation is exactly what it sounds like: rotating an image by some angle theta.
 We’ll use theta to represent by how many degrees we are rotating the image.



'''

#Grab the dimension of the image and calculate the center of the image
(h,w) = image.shape[:2]
(cX,cY) = (w/2,h/2)
#Rotate the image by 45 degree
M  = cv2.getRotationMatrix2D((cX,cY),45,2.0)
rotated = cv2.warpAffine(image,M,(w,h))
cv2.imshow("Rotated by 45 degree",rotated)

# rotate our image by -90 degrees
M = cv2.getRotationMatrix2D((cX, cY), -90, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by -90 Degrees", rotated)
# rotate our image around an arbitrary point rather than the center
M = cv2.getRotationMatrix2D((cX - 50, cY - 50), 45, 1.0)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by Offset & 45 Degrees", rotated)
# finally, let's use our helper function in imutils to rotate the image by
# 180 degrees (flipping it upside down)
rotated = imutils.rotate(image, 180)
cv2.imshow("Rotated by 180 Degrees", rotated)
cv2.waitKey(0)




