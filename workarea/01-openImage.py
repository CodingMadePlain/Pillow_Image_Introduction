# Script: 01-openImage.py
# Topic: Opening an image with Pillow and reading its dimensions
# Run from: project root (Pillow_Image_Introduction)

# Import the Image module from the PIL package
from PIL import Image

# The image file lives in the large_assets/ folder in the project root
# Since we are running from the project root, we can directly access it
img = Image.open("large_assets/large_image.jpg")

# .size returns a tuple (width, height) — here we unpack it into two variables
width, height = img.size

# Print the width value
print(f"Width: {width}")

# Print the height value
print(f"Height: {height}")

# show the image in a window
img.show()