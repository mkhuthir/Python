#!/usr/bin/python3

from PIL import Image

# Load Image
img = Image.open("../../img/fruits.jpg")

# Print specs
print (f"Format is {img.format} Size is {img.size}, and Mode is {img.mode}")

# Show image
img.show()


