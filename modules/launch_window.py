import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, UnidentifiedImageError
from modules.image_window import ImageWindow

class LaunchWindow(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        # image related info
        self.var_selected_image_path = ""

        # main window widgets
        self.label_image_info = tk.Label(self, text="Browse to select an image file")
        self.button_browse_image = tk.Button(self, text="Browse", command=self.browse_image)
        self.button_load_image = tk.Button(self, text="Load image", command=self.launch_image_window)
        self.label_image_info.pack()
        self.button_browse_image.pack()

        # misc / debug widgets
        self.button_misc = tk.Button(self, text="For testing/debugging", command=self.debug)
        # self.button_misc.pack()

    def browse_image(self): 
        file_path = filedialog.askopenfilename(initialdir = ".", 
                                title = "Select an image file", 
                                filetypes = (("Image files", ".jpg .jpeg .png .bmp .tiff"), 
                                ("All files", "*.*")))
        try:
            _ = Image.open(file_path)
            self.label_image_info.configure(text="Image file read: "+".../"+(file_path.split('/')[-1]))
            self.var_selected_image_path = file_path
            # successful read of image, display button to load image window
            self.button_load_image.pack() 
        except UnidentifiedImageError:
            self.label_image_info.configure(text="Error reading image file")
            self.var_selected_image_path = ""
            self.button_load_image.pack_forget()
        except AttributeError:
            self.label_image_info.configure(text="Browse to select an image file")
            self.var_selected_image_path = ""
            self.button_load_image.pack_forget()

    def launch_image_window(self):
        self.new_window = tk.Toplevel(self.parent)
        var_title = "Python Image Tool - {}".format(self.var_selected_image_path)
        self.new_window.title(var_title)
        self.image_window = ImageWindow(self.new_window,self.var_selected_image_path)
    
    def debug(self):
        print("Use this function for debugging")
