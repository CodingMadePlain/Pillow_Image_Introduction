# Import the Image module from the PIL package
from PIL import Image

# Import the TAGS dictionary for converting numeric IDs to readable names
from PIL.ExifTags import TAGS

# Open the image file
img = Image.open("large_assets/coffee_exif_image.jpg")

# Get the raw EXIF data
exif_data = img._getexif()

# Define a set of tag names we want to display — sets are faster for lookups than lists
wanted_tags = {
    "ImageDescription",
    "Model",
    "ShutterSpeedValue",
    "DateTimeOriginal",
    "Artist"
}

# Check if EXIF data exists
if exif_data:

    # Loop through all EXIF tags
    for tag_id, value in exif_data.items():

        # Convert the numeric ID to a readable name
        tag_name = TAGS.get(tag_id, tag_id)

        # Only print this tag if it is in our wanted set
        if tag_name in wanted_tags:
            print(f"{tag_name}: {value}")
else:
    print("No EXIF data found")

# Next, we'll see how to write data back to the image in 01-exifWriting.py