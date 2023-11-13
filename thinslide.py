from PIL import Image
import os

testslide0 = os.getcwd() + f"{os.sep}thinslides{os.sep}0.jpg"
testslide1 = os.getcwd() + f"{os.sep}thinslides{os.sep}1.jpg"


class ColorRelation:
    def __init__(self, color):
        self.color = color
        self.related = []

        for shade_index in range(0, 3):
            for i in range(1, 5):
                newcolor = [*self.color]
                newcolor_dn = [*self.color]
                newcolor[shade_index] += i
                newcolor_dn[shade_index] -= i
                self.related.append(tuple(newcolor))
                self.related.append(tuple(newcolor_dn))


class ColorOccurence:
    def __init__(self, color, occurence=0):
        self.color = color
        self.occurence = occurence

class ColorFrequency:
    def __init__(self, color):
        self.color = color
        self.frequency = 0
    def increment_if_color(self, color):
        if color == self.color:
            self.frequency += 1

class ImagePixels:
    def __init__(self, filepath:str):
        img = Image.open(filepath)
        self.width, self.height = img.size
        # Get the pixel data
        _pixels = list(img.getdata())
        # If the image has multiple channels (e.g., RGB), flatten the list
        if img.mode in ('RGB', 'RGBA'):
            _pixels = [pixel[:3] for pixel in _pixels]
        self.pixels = [px for px in _pixels if px!=_pixels[0]]
        self.palette = list(set(self.pixels))
        self.num_pixels = len(self.pixels)
        self.num_colors = len(self.palette)
        self.color_frequency = {}
        for px in self.pixels:
            try:
                self.color_frequency[px]+=1
            except KeyError:
                self.color_frequency[px] = 1
        self.abundant_colors = [name for name, value in self.color_frequency.items() if value > 5]
        self.color_occurrences = [ColorOccurence(name, value) for name, value in self.color_frequency.items()]
        self.num_abundant_colors = len(self.abundant_colors)

        self.related_colors = [ColorRelation(px) for px in self.pixels]]
    
    def print_abundant_colors(self):
        for px in self.abundant_colors:
            print(px)
        print(self.num_abundant_colors)

    
    def print_frequency(self):
        for name, value in self.color_frequency.items():
            print(f"color: {name} \t count: {value}")

    
    def print(self):
        for px in self.pixels:
            print(px)

    def print_palette(self):
        for px in self.palette:
            print(px)

    def print_info(self):
        print(f"pixel count: {self.num_pixels}\npalette count: {self.num_colors}\nimage width: {self.width}\nimage height: {self.height}")


    def relate_colors(self):
        retv = []
        for rc in self.related_colors


def image_to_pixel_list(filepath: str) -> list:
    # Open the image
    img = Image.open(filepath)

    # Get the pixel data
    pixel_data = list(img.getdata())

    # If the image has multiple channels (e.g., RGB), flatten the list
    if img.mode in ('RGB', 'RGBA'):
        pixel_data = [pixel[:3] for pixel in pixel_data]

    return pixel_data




