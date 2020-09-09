import tkinter as tk
from PIL import Image, ImageTk
from modules.image_manip import (grayscale, flip_v, flip_h, gaussian_blur, mean_blur, laplacian, 
                        sobel, sharpen, threshold_fixed, threshold_otsu_binary, threshold_otsu,
                        erosion, dilation)

class ImageWindow(tk.Frame):
    def __init__(self, parent, image_path, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.var_image_path = image_path
        self.var_image = Image.open(self.var_image_path)
        self.var_image_factor = 1
        self.var_image_stack = []
        self.label_image = tk.Label(self.parent)
        self.menu_bar = tk.Menu(self)
        self.normalize_resolution()
        self.display_image()
        self.load_menubar()

    def normalize_resolution(self):
        var_image_width, var_image_height = self.var_image.size
        var_window_width, var_window_height = self.winfo_screenwidth(), self.winfo_screenheight()
        var_width_factor = var_image_width / var_window_width
        var_height_factor = var_image_height / var_window_height
        if ((var_height_factor > 1) or (var_width_factor > 1)):
            self.var_image_factor = var_width_factor if var_width_factor > var_height_factor  else var_height_factor
            var_image_width, var_image_height = int(var_image_width / self.var_image_factor), int(var_image_height / self.var_image_factor)
            self.var_image = self.var_image.resize((var_image_width, var_image_height))
        self.var_image_stack.append(self.var_image)

    def display_image(self):
        var_image = ImageTk.PhotoImage(self.var_image)
        self.label_image.configure(image=var_image)
        self.label_image.image = var_image
        self.label_image.pack(side="top", fill="both", expand="no")

    def menubar_file_undo(self):
        if(len(self.var_image_stack) > 1):
            self.var_image_stack.pop(-1)
            self.var_image = self.var_image_stack[-1]
        self.display_image()

    def menubar_file_save_as(self):
        var_types_extensions = [('PNG file','*.png')]
        try:
            var_save_file = tk.filedialog.asksaveasfile("wb", filetypes=var_types_extensions, defaultextension=var_types_extensions)
            self.var_image  = self.var_image.resize((int(self.var_image.size[0]*self.var_image_factor), int(self.var_image.size[1]*self.var_image_factor)))
            self.var_image.save(var_save_file, format='PNG')
        except AttributeError:
            pass
    
    def menubar_image_convert_grayscale(self):
        self.var_image = grayscale(self.var_image)
        self.var_image_stack.append(self.var_image)
        self.display_image()

    def menubar_image_flip_v(self):
        self.var_image = flip_v(self.var_image)
        self.var_image_stack.append(self.var_image)
        self.display_image()

    def menubar_image_flip_h(self):
        self.var_image = flip_h(self.var_image)
        self.var_image_stack.append(self.var_image)
        self.display_image()

    def menubar_blur_gaussian(self):
        # TODO prompt for no. of pixels (neighbourhood, default is 2)
        self.var_image = gaussian_blur(self.var_image)
        self.var_image_stack.append(self.var_image)
        self.display_image()
    
    def menubar_blur_mean(self):
        self.var_image = mean_blur(self.var_image)
        self.var_image_stack.append(self.var_image)
        self.display_image()

    def menubar_blur_sharpen(self):
        self.var_image = sharpen(self.var_image)
        self.var_image_stack.append(self.var_image)
        self.display_image()

    def menubar_edge_detection_laplacian(self):
        self.var_image = laplacian(self.var_image)
        self.var_image_stack.append(self.var_image)
        self.display_image()
    
    def menubar_edge_detection_sobel(self):
        self.var_image = sobel(self.var_image)
        self.var_image_stack.append(self.var_image)
        self.display_image()

    def menubar_threshold_fixed(self):
        # TODO prompt for threshold value
        self.var_image = threshold_fixed(self.var_image)
        self.var_image_stack.append(self.var_image)
        self.display_image()
    
    def menubar_threshold_otsu(self):
        self.var_image = threshold_otsu(self.var_image)
        self.var_image_stack.append(self.var_image)
        self.display_image()
    
    def menubar_threshold_otsu_binary(self):
        self.var_image = threshold_otsu_binary(self.var_image)
        self.var_image_stack.append(self.var_image)
        self.display_image()

    def menubar_morphological_erosion(self):
        # TODO prompt for size value
        self.var_image = erosion(self.var_image)
        self.var_image_stack.append(self.var_image)
        self.display_image()

    def menubar_morphological_dilation(self):
        # TODO prompt for size value
        self.var_image = dilation(self.var_image)
        self.var_image_stack.append(self.var_image)
        self.display_image()

    # add new method here

    def load_menubar(self):
        menu_file = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=menu_file)
        menu_file.add_command(label="Undo", command=self.menubar_file_undo)
        menu_file.add_command(label="Save As", command=self.menubar_file_save_as)
        menu_file.add_command(label="Close File", command=self.parent.destroy)
        
        menu_image = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Image", menu=menu_image)
        menu_image.add_command(label="Convert To Grayscale", command=self.menubar_image_convert_grayscale)
        menu_image.add_command(label="Flip Vertically", command=self.menubar_image_flip_v)
        menu_image.add_command(label="Flip Horizontally", command=self.menubar_image_flip_h)
        
        menu_blur = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Blur / Sharpen", menu=menu_blur)
        menu_blur.add_command(label="Gaussian Blur", command=self.menubar_blur_gaussian)
        menu_blur.add_command(label="Mean Blur", command=self.menubar_blur_mean)
        menu_blur.add_command(label="Sharpen", command=self.menubar_blur_sharpen)

        menu_edge_detection = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Edge Detection", menu=menu_edge_detection)
        menu_edge_detection.add_command(label="Laplacian Operator", command=self.menubar_edge_detection_laplacian)
        menu_edge_detection.add_command(label="Sobel Operator", command=self.menubar_edge_detection_sobel)
        
        menu_threshold = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Thresholding / Segmentation", menu=menu_threshold)
        menu_threshold.add_command(label="Fixed Threshold", command=self.menubar_threshold_fixed)
        menu_threshold.add_command(label="Otsu Threshold", command=self.menubar_threshold_otsu)
        menu_threshold.add_command(label="Otsu Threshold - Binary", command=self.menubar_threshold_otsu_binary)

        menu_morphological = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Morphological Operations", menu=menu_morphological)
        menu_morphological.add_command(label="Erosion", command=self.menubar_morphological_erosion)
        menu_morphological.add_command(label="Dilation", command=self.menubar_morphological_dilation)

        # add new menus and commands here and mention the respective method for each command, see above code for reference
        
        self.parent.config(menu=self.menu_bar)