from PIL import Image

# Open the JPG file
image = Image.open("large_assets/large_image.jpg")

# show the iamge before resizing
image.show()

# Resize to 128x72 while keeping the aspect ratio
image.thumbnail((128, 72))

# show the thumbnail image
image.show()

# Save it as a PNG file
image.save("large_images/thumbnail_image.png", "PNG")

print("Conversion and resize complete!")

