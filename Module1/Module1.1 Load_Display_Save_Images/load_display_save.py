import cv2
import numpy as np
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Path of the image")
args =  vars(ap.parse_args())


#Load the image
image = cv2.imread(args['image'])
print("width: %d pixels" % (image.shape[1]))
print("height: %d pixels" % (image.shape[0]))
print("channels: %d" % (image.shape[2]))
# show the image and wait for a keypress
cv2.imshow("Image", image)
cv2.waitKey(0)
#Save the image
cv2.imwrite("newimage.jpg",image)


