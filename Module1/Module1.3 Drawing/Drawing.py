#File to draw the different shapes on an image
#Load the all the required libraries
import cv2
import matplotlib.pyplot as plt
import argparse
import numpy as np


ap = argparse.ArgumentParser()
ap.add_argument('-i','--image',required=False,help='Pass the correct file path')
args = vars(ap.parse_args())

#Load the images 
image = cv2.imread(args['image'])
canvas = np.zeros((300, 300, 3), dtype="uint8")
#Draw a line from top left to bottom right
green=(0,255,0)
cv2.line(canvas,(0,0),(300,300),green)
cv2.imshow('Canvas',canvas)
#Draw a 3 pixel thick red line from the top right to the bottom left
red = (0,0,255)
cv2.line(canvas,(300,0),(0,300),red,3)
cv2.imshow('Canvs with red line',canvas)

#Draw a green 60 x 60 pixel square , starting at 10,10 and ending at 60,60
cv2.rectangle(canvas,(10,10),(60,60),green)
cv2.imshow('Canvas having square',canvas)

#Draw another rectangle
cv2.rectangle(canvas,(50,200),(200,225),red,5)
cv2.imshow('Thick Rectangle of Red Color',canvas)

#Draw a solid rectangle , to draw a solid rectangle pass the argument as -1
blue = (255,0,0)
cv2.rectangle(canvas,(200,50),(225,125),blue,-1)
cv2.imshow('Canvas with filled blue rectangle',canvas)

cv2.waitKey(0)
cv2.destroyAllWindows()
