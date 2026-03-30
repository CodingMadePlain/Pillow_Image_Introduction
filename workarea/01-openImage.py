# Import the Image module from the PIL package
from PIL import Image

# Open the image file and load it into memory
img = Image.open("photo.jpg")

# .size returns a tuple (width, height) — here we unpack it into two variables
width, height = img.size

# Print the width value
print(f"Width: {width}")

# Print the height value
print(f"Height: {height}")