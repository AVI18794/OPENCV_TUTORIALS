import cv2
import argparse
import numpy as np
import imutils
ap= argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Path of the image")
args =vars(ap.parse_args())

'''
Translation
Translation is the shifting of an image along the x and y axis.
Using translation, we can shift an image up, down, left, or right, 
along with any combination of the above.

Our translation matrix M is defined as a floating point array — this is important because OpenCV expects this matrix to be of floating point type. The first row of the matrix is [1, 0, t_{x}], where t_{x} is the number of pixels we will shift the image left or right. Negative values of t_{x} will shift the image to the left and positive values will shift the image to the right.

Then, we define the second row of the matrix as [0, 1, t_{y}], where t_{y} is the number of pixels we will shift the image up or down. Negative values of t_{y} will shift the image up and positive values will shift the image down.



'''
#load the image
image =cv2.imread(args['image'])
cv2.imshow("Original Image",image)
# NOTE: Translating (shifting) an image is given by a NumPy matrix in
# the form:
#	[[1, 0, shiftX], [0, 1, shiftY]]
# You simply need to specify how many pixels you want to shift the image
# in the X and Y direction -- let's translate the image 25 pixels to the
# right and 50 pixels down
M = np.float32([[1,0,25],[0,1,50]])
shifted = cv2.warpAffine(image,M,(image.shape[1],image.shape[0]))
cv2.imshow("Shifted Down and Right",shifted)

#Now let's shift the image 50 pixels to the left and 90 pixels up
M = np.float32([[1,0,-50],[0,1,-90]])
shifted = cv2.warpAffine(image,M,(image.shape[1],image.shape[0]))
cv2.imshow("Shifted Up and Left",shifted)


#Shifting the image using imutils package
shifted_imutils = imutils.translate(image,0,100)
cv2.imshow("Shifted Down",shifted_imutils)
cv2.waitKey(0)
cv2.destroyAllWindows()