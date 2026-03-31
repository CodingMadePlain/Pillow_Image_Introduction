# Import the Image module from the PIL package
from PIL import Image

# Open the image file
img = Image.open("large_assets/large_image.jpg")

# Resize to exactly 600x500 pixels — returns a NEW image, does not change the original
resized_img = img.resize((600, 500))

# Save the new resized image to a file
resized_img.save("large_images/resized_photo.jpg")

# Print size of resized image
print("Resized image size:", resized_img.size)

# show the resized image
#resized_img.show()

# next we will use the thumbnail method to resize - 01-thumbnail.py