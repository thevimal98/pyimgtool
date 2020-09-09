# pyimgtool
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

## Installation and modifications
* Clone the repo, change directory, install the requirements and run `python main.py`
* Modifications can be done via the ImageWindow class in `image_window.py` by adding methods as specified (check comments)
* For readability, clarity and refactor purposes, the actual image manipulation code is specified in `image_manip.py`

## Sample outputs
* TODO

## References
* To structure the tkinter application - https://stackoverflow.com/a/17470842
* tkinter widget related info - https://www.geeksforgeeks.org/python-gui-tkinter/
* Image operations using ImageOps (Pillow) - https://pillow.readthedocs.io/en/3.0.x/reference/ImageOps.html
* Image operations using ImageFilter (Pillow) - https://pillow.readthedocs.io/en/5.1.x/reference/ImageFilter.html
* Otsu thresholding code - https://stackoverflow.com/a/50796152
