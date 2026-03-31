# Script: sample_compress.py
# Topic: Compress an image by reducing its save quality
# Run from: workarea/

from PIL import Image
import os

# Open the original large image
original_image = Image.open("large_assets/coffee_cup.jpg")
print("Original image opened.")

# Save the image with a lower quality setting to compress the file size.
# The 'quality' parameter ranges from 1 (worst) to 95 (best). A value of 60 
# reduces the file size significantly while retaining acceptable visual quality.
# The 'optimize' flag applies extra compression steps.
original_image.save(
    "large_images/compressed_coffee_cup.jpg", 
    format="JPEG", 
    optimize=True, 
    quality=60
)

print("Image compressed and saved successfully.")