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

'''Scaling , or simply resizing , is the process of increasing or decreasing
the size of an image in terms of the width and height.

When resizing an image, it’s important to keep in mind the aspect ratio — which is the 
ratio of the width of the image to the height of an image.
Ignoring the aspect ratio can lead to resized images that look compressed and distorted:'''

# we need to keep in mind aspect ratio so the image does not look skewed
# or distorted -- therefore, we calculate the ratio of the new image to
# the old image. Let's make our new image have a width of 150 pixels

r = 150.0/image.shape[1]
dim = (150,int(image.shape[0]*r))
#Perform the actual resizing of the image
resized = cv2.resize(image,dim,interpolation=cv2.INTER_AREA)
cv2.imshow("Resized(Width) Image",resized)
# what if we wanted to adjust the height of the image? We can apply
# the same concept, again keeping in mind the aspect ratio, but instead
# calculating the ratio based on height -- let's make the height of the
# resized image 50 pixels
r = 50.0 / image.shape[0]
dim = (int(image.shape[1] * r), 50)
# perform the resizing
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized (Height)", resized)
# of course, calculating the ratio each and every time we want to resize
# an image is a real pain -- let's create a  function where we can specify
# our target width or height, and have it take care of the rest for us.
resized = imutils.resize(image, width=100)
cv2.imshow("Resized via Function", resized)
# construct the list of interpolation methods
methods = [
	("cv2.INTER_NEAREST", cv2.INTER_NEAREST),
	("cv2.INTER_LINEAR", cv2.INTER_LINEAR),
	("cv2.INTER_AREA", cv2.INTER_AREA),
	("cv2.INTER_CUBIC", cv2.INTER_CUBIC),
	("cv2.INTER_LANCZOS4", cv2.INTER_LANCZOS4)]
# loop over the interpolation methods
for (name, method) in methods:
	# increase the size of the image by 3x using the current interpolation
	# method
	resized = imutils.resize(image, width=image.shape[1] * 3, inter=method)
	cv2.imshow("Method: {}".format(name), resized)
cv2.waitKey(0)
cv2.destroyAllWindows()


