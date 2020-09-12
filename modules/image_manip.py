from PIL import Image, ImageFilter, ImageOps
import numpy as np

def grayscale(image):
    return image.convert('LA')

def flip_v(image):
    return image.transpose(method=Image.FLIP_LEFT_RIGHT)

def flip_h(image):
    return image.transpose(method=Image.FLIP_TOP_BOTTOM)

def gaussian_blur(image, rad=2):
    return image.filter(ImageFilter.GaussianBlur(radius=rad))

def mean_blur(image):
    kernel_mean_blur = (
                    1, 1, 1,
                    1, 1, 1,
                    1, 1, 1
                    )
    k = ImageFilter.Kernel(size=(3, 3), kernel=kernel_mean_blur, scale=sum(kernel_mean_blur))
    return image.filter(k)

def sharpen(image):
    return image.filter(ImageFilter.SHARPEN)


def laplacian(image):
    image = gaussian_blur(grayscale(image)) # preprocess to remove noise
    kernel_laplacian = (
                    -1, -1, -1,
                    -1, 8, -1,
                    -1, -1, -1
                    )
    k = ImageFilter.Kernel(size=(3, 3), kernel=kernel_laplacian, scale=1)
    return image.filter(k)

def sobel(image):
    image = grayscale(image)
    kernel_sobel_x = (
                    -1, 0, 1,
                    -2, 0, 2,
                    -1, 0, 1
                    )
    kernel_sobel_y = (
                    1, 2, 1,
                    0, 0, 0,
                    -1, -2, -1
                    )
    k = ImageFilter.Kernel(size=(3,3), kernel=kernel_sobel_x, scale=1)
    image = image.filter(k)
    k = ImageFilter.Kernel(size=(3,3), kernel=kernel_sobel_y, scale=1)
    return image.filter(k)

def threshold_fixed(image):
    thresh = 170
    return image.point(lambda  p: p > thresh and 255)

def otsu(image, binary=False): # got this from Stack Overflow - https://stackoverflow.com/a/50796152
    if(binary):
        image = grayscale(image) # preprocess to remove noise
    gray = gaussian_blur(image)
    gray = np.asarray(gray)
    pixel_number = gray.shape[0] * gray.shape[1]
    mean_weigth = 1.0/pixel_number
    his, bins = np.histogram(gray, np.arange(0,257))
    final_thresh = -1
    final_value = -1
    intensity_arr = np.arange(256)
    for t in bins[1:-1]: # This goes from 1 to 254 uint8 range (Pretty sure wont be those values)
        pcb = np.sum(his[:t])
        pcf = np.sum(his[t:])
        Wb = pcb * mean_weigth
        Wf = pcf * mean_weigth

        mub = np.sum(intensity_arr[:t]*his[:t]) / float(pcb)
        muf = np.sum(intensity_arr[t:]*his[t:]) / float(pcf)
        #print mub, muf
        value = Wb * Wf * (mub - muf) ** 2

        if value > final_value:
            final_thresh = t
            final_value = value
    final_img = gray.copy()
    # print(final_thresh)
    if(binary):
        final_img[gray > final_thresh] = 255
    final_img[gray < final_thresh] = 0
    return Image.fromarray(np.uint8(final_img))

def threshold_otsu_binary(image):
    return otsu(image,binary=True)

def threshold_otsu(image):
    return otsu(image)

def erosion(image):
    return image.filter(ImageFilter.MinFilter)

def dilation(image):
    return image.filter(ImageFilter.MaxFilter)

def invert(image):
    if(image.mode=="LA"):
        return ImageOps.invert(image.convert('L'))
    return ImageOps.invert(image)