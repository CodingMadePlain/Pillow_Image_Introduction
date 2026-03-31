# Import the Image module from the PIL package
from PIL import Image

# Import piexif — a separate library for writing EXIF data (pip install piexif)
import piexif

# Open the image file
img = Image.open("large_assets/coffee_exif_image.jpg")

# Load existing EXIF data into a dictionary — if none exists, start with empty bytes
exif_dict = piexif.load(img.info.get("exif", b""))

# Add the ImageDescription tag to the "0th" section
exif_dict["0th"][piexif.ImageIFD.ImageDescription] = "A splendid cup of Coffee"

# Convert the dictionary back into raw bytes that can be embedded in an image
exif_bytes = piexif.dump(exif_dict)

# Save the image with the updated EXIF data
img.save("large_images/updated_photo.jpg", exif=exif_bytes)
print("EXIF data updated and image saved as 'large_images/updated_photo.jpg'")