# Import the Image module from the PIL package
from PIL import Image

# Open the image file
img = Image.open("large_assets/large_image.jpg")

# Shrink the image to fit within 600x500 — modifies the image IN PLACE, no new image returned
img.thumbnail((600, 500))

# Save the modified image to large_imahes/ folder with a new name
img.save("large_images/thumbnail_image.jpg")

# show the thumbnail image
img.show()

# Next, we will look at how to read EXIF data - see 01-exifData.py