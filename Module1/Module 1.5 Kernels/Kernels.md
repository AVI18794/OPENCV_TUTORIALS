Well if we think of an image as a big matrix, then we can think of a kernel or convolutional matrix as a tiny matrix that is used for blurring, sharpening, edge detection, and other image processing functions.

Essentially, this tiny kernel sits on top of the big image and slides from left to right and up to down, applying a mathematical operation at each (x, y)-coordinate in the original image. Again, by applying kernels to images we are able to blur and sharpen them, similar to if we were editing an image in Photoshop.

We can also use convolution to extract features from images and build very powerful deep learning systems.

#Image Kernels
So let's assume our image is a big matirx and kernel is as a tiny matrix(at least in comparion to the images which is a bigger matrix.)
See in the figure below</br>
![Kernel and Image Matrix]("Images\kernel_sliding.png")
</br>
As you see in the figure the kernels or filters are sliding from let to right and top to bottom along the original image.
At each point (x,y)-coordinate of the image we stop and examine the neighbour of the image pixels located at the center of the image kernel.

We can take this neighborhood of pixels, convolve them with the kernel, and we get a single output value. This output value is then stored in the output image at the same (x, y)-coordinate as the center of the kernel.

