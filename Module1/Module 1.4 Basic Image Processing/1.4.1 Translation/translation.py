import cv2
import argparse

ap= argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Path of the image")
args =vars(ap.parse_args())

