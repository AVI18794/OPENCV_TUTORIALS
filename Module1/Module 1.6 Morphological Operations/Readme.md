# Morphological Operations
Morphological operations are simple transformations applied to binary or grayscale images.

More specifically, we apply morphological operations to shapes and structures inside of images. We can use morphological operations to increase the size of objects in images as well as decrease them. We can also utilize morphological operations to close gaps between objects as well as open them.

Morphological operations “probe” an image with a structuring element. This structuring element defines the neighborhood to be examined around each pixel. And based on the given operation and the size of the structuring element we are able to adjust our output image.

This may sound vague. That’s because it is. There are many different morphological transformations that perform “opposite” operations from one another — just as addition is the “opposite” of subtraction, we can think of the erosion morphological operation as the “opposite” of dilation.

The most important component that makes morphological operations possible is structuring element.
#Structuring element
Well, you can (conceptually) think of a structuring element as a type of kernel or mask. However, instead of applying a convolution, we are only going to perform simple tests on the pixels.

And just like in image kernels, the structuring element slides from left-to-right and top-to-bottom for each pixel in the image. Also just like kernels, structuring elements can be of arbitrary neighborhood sizes.

We can make any arbitrary structuring element which is circular, rectangular or of any arbitrary shapes- it depends on the applications.
In OpenCV, we can either use the **cv2.getStructuringElement**  function or NumPy itself to define our structuring element.


**In simpler terms:-A structuring element behaves similar to a kernel or a mask- but instead of convolving the input image with our structuring element, we are just going to be applying simple pixel tests.**
There are different types of morphological operations which can be perfomed on the image. We will discuss them one by one.
* Erosion
* Dilation
* Opening
* Closing
* Morphological gradient
* Black hat
* Top hat (or “White hat”)

## Erosion
Just like water rushing along a river bank erodes the soil, an erosion in an image “erodes” the foreground object and makes it smaller. Simply put, pixels near the boundary of an object in an image will be discarded, “eroding” it away.

Erosion works by defining a structuring element and then sliding this structuring element from left-to-right and top-to-bottom across the input image.

A foreground pixel in the input image will be kept only if ALL pixels inside the structuring element are > 0. Otherwise, the pixels are set to 0 (i.e. background).

Erosion is useful for removing small blobs in an image or disconnecting two connected objects.

We can perform erosion by using the cv2.erode  function.
