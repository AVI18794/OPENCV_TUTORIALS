#import all the required libraries
import cv2
import matplotlib.pyplot as plt


#Load the images from the directory
image = cv2.imread('Data/Images/fig1.jpg')
#Convert the image into grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# load the face detector and detect faces in the image
detector = cv2.CascadeClassifier("Data/haarcascade_frontalface_default.xml")
rects = detector.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=9,
	minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)

# loop over the faces and draw a rectangle surrounding each
for (x, y, w, h) in rects:
	cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# show the detected faces
cv2.imshow("Faces", image)
cv2.waitKey(0)