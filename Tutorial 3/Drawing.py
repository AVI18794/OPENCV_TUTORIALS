#File to draw the different shapes on an image
#Load the all the required libraries
import cv2
import matplotlib.pyplot as plt
import argparse
import numpy as np


ap = argparse.ArgumentParser()
ap.add_argument('-i','--image',required=True,help='Pass the correct file path')
args = vars(ap.parse_args())

#Load the images 
image = cv2.imread(args['image']])
canvas = np.zeros((300, 300, 3), dtype="uint8")
