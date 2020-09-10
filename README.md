# pyimgtool [![HitCount](http://hits.dwyl.com/thevimal98/pyimgtool.svg)](http://hits.dwyl.com/thevimal98/pyimgtool)
Python Image Tool - a tkinter based CVIPtools like application for image processing.

## What is pyimgtool?
It's a tkinter based GUI application to perform image processing.

## What can pyimgtool do?
The application let's you load image files (PIL supported) and perform operations -
* Basic
  * Flip the image
  * Convert to grayscale
  * Undo an operation
  * Save as (a PNG file)
* Blur/sharpen
  * Gaussian, Mean filters
  * PIL ImageFilter filters
* Edge detection
  * Laplacian, Sobel operators
* Thresholding
  * Fixed threshold
  * Otsu threshold - binary and otherwise
* Morphological
  * Erosion, dilation

The OO design nature of this application allows easy addition of operations and code refactoring (maybe from PIL to OpenCV)

## Why pyimgtool?
A fast track way to observe an image and operations performed on it. The idea for this application came during my senior year, after I completed a course in Computer Vision, where I learned about a lot of the operations included here. I've also wanted to implement a multi-window tkinter application with shared namespaces (just for fun), so I figured, might as well go for an application of this nature.

## Requirements
* Python3 (tested on 3.6.7)
* numpy (tested on 1.19.1)
* Pillow (tested on 7.2.0)

## Installation, usage and modifications
* Clone the repo, change directory, install the requirements and run `python main.py`
  * If you're using `pip`, install the requirements using `pip install -r requirements.txt`
* Modifications can be done via the ImageWindow class in `image_window.py` by adding methods as specified (check comments)
* For readability, clarity and refactor purposes, the actual image manipulation code is specified in `image_manip.py`

## Sample outputs
#### Image - ./data/samples/shapes.jpg

<img src="https://github.com/thevimal98/pyimgtool/blob/master/data/screenshots/loaded_shapes.JPG" width=50% height=50%>

* After applying Gaussian Blur operation

<img src="https://github.com/thevimal98/pyimgtool/blob/master/data/screenshots/loaded_shapes_GB.JPG" width=50% height=50%>

* After applying Binary Otsu Thresholding operation

<img src="https://github.com/thevimal98/pyimgtool/blob/master/data/screenshots/loaded_shapes_BOT.JPG" width=50% height=50%>

#### Image - ./data/samples/a.jpg

<img src="https://github.com/thevimal98/pyimgtool/blob/master/data/screenshots/loaded_a.JPG" width=50% height=50%>

* After applying Erosion operation

<img src="https://github.com/thevimal98/pyimgtool/blob/master/data/screenshots/loaded_a_erosion.JPG" width=50% height=50%>

* After applying Dilation operation

<img src="https://github.com/thevimal98/pyimgtool/blob/master/data/screenshots/loaded_a_dilation.JPG" width=50% height=50%>

## References
* To structure the tkinter application - https://stackoverflow.com/a/17470842
* tkinter widget related info - https://www.geeksforgeeks.org/python-gui-tkinter/
* Image operations using ImageOps (Pillow) - https://pillow.readthedocs.io/en/3.0.x/reference/ImageOps.html
* Image operations using ImageFilter (Pillow) - https://pillow.readthedocs.io/en/5.1.x/reference/ImageFilter.html
* Otsu thresholding code - https://stackoverflow.com/a/50796152
* Thresholding - overview - https://datacarpentry.org/image-processing/07-thresholding/
