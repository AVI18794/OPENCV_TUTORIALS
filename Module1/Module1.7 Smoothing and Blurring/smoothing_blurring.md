# Smoothing and Blurring
Smoothing and blurring is one of the most important pre-processing steps in all of computer vision and image processing.By smoothing an image we are reducing the high frequency content, such as nouse and edges(i.e. details of an image).
There are many types of smoothing or blurring but the most commonly used ones are as follows:-

* Averaging
* Gaussian Blurring
* Median Filtering
* Bilateral Filtering


## Averaging
An average filter takes the average of the region surrounding a pixel and smooth it and replace it with the value of its local neighborhood.


**As the size of the kernel increases, so will the amount in which the image is blurred.**
In order to average blur an image , we use the cv2.blur function.The function requires two arguments :
  1) The image we want to blur 
  2) The size of the kernel.
  
