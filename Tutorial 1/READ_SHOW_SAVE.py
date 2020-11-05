#Import all the required librabries
import cv2
import argparse
#Construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument('-i','--image',required=True,help='Pass the correct path of Image ')
args = vars(ap.parse_args())

#Load the images from the path
image = cv2.imread(args['image'])
#Print the info related to the loaded images
print('Width %d pixels' %(image.shape[1]))
print('Height %d pixels '%(image.shape[0]))
print('No. of Channels : %d' %(image.shape[2]))

#Display the image and wait for sometime
cv2.imshow('Image',image)
cv2.waitKey(0)

#Save the image into the location with other name
cv2.imwrite('../Data/Images/newimage.jpg',image)
#Close all the windows
cv2.destroyAllWindows()
