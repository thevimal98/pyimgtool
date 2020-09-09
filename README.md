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
- TODO

## Installation
- TODO

## Sample outputs
- TODO
