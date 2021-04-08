#Import all the required libraries
import cv2
import matplotlib.pyplot as plt
import argparse

#Create the argparse object and parse the object
ap = argparse.ArgumentParser()
ap.add_argument('-i','--image',help='Path to the input image',required=True)
args= vars(ap.parse_args())

#Load the images
image = cv2.imread(args['image'])
#Get the dimensions of the image
(h,w) = image.shape[:2]
cv2.imshow("Original Image",image)

# images are just NumPy arrays. The top-left pixel can be found at (0, 0)
(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {r}, Green: {g}, Blue: {b}".format(r=r, g=g, b=b))
# now, let's change the value of the pixel at (0, 0) and make it red
image[0, 0] = (0, 0, 255)
(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {r}, Green: {g}, Blue: {b}".format(r=r, g=g, b=b))

#Computing the center of the image 
(cX,cY)=(w//2,h//2)

#since the numpy arrays are being used, we can apply slicing and grab the larger chunks
#Slicing of the image
tl = image[0:cY,0:cX]
#Display the image
cv2.imshow('Top Left Corner of the Image',tl)

#Grab the other parts of the image(top right,bottom right,, bottom left)
tr = image[0:cY,cX:w]
br = image[cY:h,cX:w]
bl = image[cY:h,0:cX]
cv2.imshow('Top-Right Corner',tr)
cv2.imshow('Bottom-Right Corner',br)
cv2.imshow('Bottom-Left Corner',bl)
image[0:cY, 0:cX] = (0, 255, 0)
# Show our updated image
cv2.imshow("Updated", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
