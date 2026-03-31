from PIL import Image

# Open the JPG file
image = Image.open("large_assets/large_image.jpg")

# Resize to 1280x720 while keeping the aspect ratio
image.thumbnail((1280, 720))

# Save it as a PNG file
image.save("large_assets/thumbnail_image.png", "PNG")

print("Conversion and resize complete!")

# show the thumbnail image
image.show()