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
  
 ## Gaussian Blur
 
  Gaussian blurring is similar to average blurring, but instead of using a simple mean, we are now using a weighted mean, where neighborhood pixels that are closer to the central pixel contribute more “weight” to the average. And as the name suggests, Gaussian smoothing is used to remove noise that approximately follows a Gaussian distribution.
The end result is that our image is less blurred, but more naturally blurred, than using the average blur method.

Furthermore, based on this weighting we’ll be able to preserve more of the edges in our image as compared to average smoothing. Just like an average blurring, Gaussian smoothing also uses a kernel of M x N, where both M and N are odd integers.


## Median Blur
The median blur method has been most effective when removing salt-and-pepper noise from the image.

When applying a median blur, we first define our kernel size . Then, as in the averaging blurring method, we consider all pixels in the neighborhood of size K x K where K is an odd integer. Notice how, unlike average blurring and Gaussian blurring where the kernel size could be rectangular, the kernel size for the median must be square. Furthermore (unlike the averaging method), instead of replacing the central pixel with the average of the neighborhood, we instead replace the central pixel with the median of the neighborhood.

The reason median blurring is more effective at removing salt-and-pepper style noise from an image is that each central pixel is always replaced with a pixel intensity that exists in the image. And since the median is robust to outliers, the salt-and-pepper noise will be less influential to the median than another statistical method, such as the average.

Again, methods such as averaging and Gaussian compute means or weighted means for the neighborhood — this average pixel intensity may or may not be present in the neighborhood. But by definition, the median pixel must exist in our neighborhood. By replacing our central pixel with a median rather than an average, we can substantially reduce noise.

Applying a median blur is accomplished by making a call to the cv2.medianBlur  function. This method takes two parameters: the image we want to blur and the size of our kernel.

## Bilateral Filtering/Blurring

In order to reduce noise while still maintaining edges, we can use bilateral blurring. Bilateral blurring accomplishes this by introducing two Gaussian distributions.

The first Gaussian function only considers spatial neighbors. That is, pixels that appear close together in the (x, y)-coordinate space of the image. The second Gaussian then models the pixel intensity of the neighborhood, ensuring that only pixels with similar intensity are included in the actual computation of the blur.

 This method is able to preserve edges of an image, while still reducing noise. The largest downside to this method is that it is considerably slower than its averaging, Gaussian, and median blurring counterparts.We can apply bilateral filtering by making a call to the cv2.bilateralFilter() function and it takes.
 
 The first parameter we supply is the image we want to blur. Then, we need to define the diameter of our pixel neighborhood — the larger this diameter is, the more pixels will be included in the blurring computation. Think of this parameter as a square kernel size.

The third argument is our color standard deviation, denoted as sigma color. A larger value for sigma color means that more colors in the neighborhood will be considered when computing the blur. If we let sigma color get too large in respect to the diameter, then we essentially have broken the assumption  of bilateral filtering — that only pixels of similar color should contribute significantly to the blur.

Finally, we need to supply the space standard deviation, which we call sigma space. A larger value of sigma space means that pixels farther out from the central pixel diameter will influence the blurring calculation.
