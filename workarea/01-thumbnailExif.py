# Import the Image module from the PIL package and piexif for EXIF metadata
from PIL import Image
import piexif

# Open the image file
img = Image.open("large_assets/compressed_coffee_cup.jpg")

# Shrink the image to fit within 600x500 — modifies the image IN PLACE, no new image returned
img.thumbnail((600, 500))

# Create an empty dictionary to hold the new EXIF data
exif_dict = {"0th": {}, "Exif": {}, "GPS": {}, "1st": {}, "Interop": {}}

# Add information to the Image IFD (0th) for general properties like Artist
exif_dict["0th"][piexif.ImageIFD.Artist] = b"Dele Oke"

# Add information to the Exif IFD for photo-specific properties
exif_dict["Exif"][piexif.ExifIFD.ISOSpeedRatings] = 127
exif_dict["Exif"][piexif.ExifIFD.WhiteBalance] = 0
exif_dict["Exif"][piexif.ExifIFD.LensMake] = b"Google"
exif_dict["Exif"][piexif.ExifIFD.LensModel] = b"Pixel 8 Pro back camera 2.23mm f/1.95"
exif_dict["Exif"][piexif.ExifIFD.DigitalZoomRatio] = (201, 100) # Stored as a ratio (fraction)
exif_dict["Exif"][piexif.ExifIFD.FocalLengthIn35mmFilm] = 12
exif_dict["Exif"][piexif.ExifIFD.ShutterSpeedValue] = (464, 100) # Stored as a ratio
exif_dict["Exif"][piexif.ExifIFD.DateTimeOriginal] = b"2026:03:02 16:54:45"

# Convert the dictionary into raw bytes so Pillow can save it
exif_bytes = piexif.dump(exif_dict)

# Save the modified image with the new EXIF data
img.save("large_images/thumbnail_exif_image.jpg", format="JPEG", exif=exif_bytes)
print("Thumbnail saved with new EXIF data.")

# show the thumbnail image
img.show()

# Next, we will look at how to read EXIF data - see 01-exifData.py