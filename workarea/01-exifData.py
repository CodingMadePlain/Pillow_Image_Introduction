# Import the Image module from the PIL package
from PIL import Image

# Import TAGS — a dictionary that maps numeric EXIF tag IDs to readable names
from PIL.ExifTags import TAGS

# Open the image file
img = Image.open("large_assets/coffee_cup.jpg")

# Get the raw EXIF data as a dictionary (keys are numeric tag IDs)
exif_data = img._getexif()

# Check if EXIF data exists before trying to loop through it
if exif_data:

    # Loop through each tag ID and its value in the EXIF dictionary
    for tag_id, value in exif_data.items():

        # Convert the numeric tag ID to a human-readable name
        tag_name = TAGS.get(tag_id, tag_id)

        # Print the tag name and its value
        print(f"{tag_name}: {value}")
else:
    # No EXIF data was found in this image
    print("No EXIF data found")

# next, we'll filter this output to only show specific tags - see 01-exifSpecific.py