# Introduction to Image Manipulation with Python Pillow

## What is Pillow?

Pillow is a Python library for opening, manipulating, and saving image files. It is a modern, maintained *fork* of the original **PIL** (Python Imaging Library), which is no longer actively developed.

Even though we install **Pillow**, we import it using `PIL` in our code. This is because Pillow was designed as a drop-in replacement for the original PIL library, so it kept the same package name.

### Installing Pillow

```bash
pip install pillow
```

### Other Libraries We Will Use Later

As the course progresses, we will combine Pillow with other libraries. You don't need to install these just yet, but it's good to know they exist.

- **os** — built into Python, used for working with files and folders (renaming, listing, creating directories)
- **numpy** — used for advanced pixel-level manipulation, treating images as arrays of numbers
- **piexif** — used for writing and editing EXIF metadata embedded in photos

## images we are using

```
- [large image](https://pixabay.com/photos/street-walking-photography-urban-4846133/) 5806 X 1280
- [graffiti-dog](https://pixabay.com/photos/graffiti-dog-wall-artwork-urban-4389452/) 3397 X 3692
```

---

## Opening an Image and Reading Its Dimensions

```python
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
```

`Image.open()` loads the image file into memory. The `.size` property returns a tuple of `(width, height)` in pixels. Here we unpack that tuple into two separate variables so we can print each one clearly.

---

## Displaying an Image

```python
# Import the Image module from the PIL package
from PIL import Image

# Open the image file and load it into memory
img = Image.open("photo.jpg")

# Unpack the width and height from the .size tuple
width, height = img.size

# Print the dimensions - f-string (short for formatted string).
print(f"Width: {width}")
print(f"Height: {height}")

# Open the image in your system's default image viewer
img.show()
```

`.show()` opens the image in your system's default image viewer. It creates a temporary file behind the scenes and launches the viewer. It is useful for quick previews during development but not something you would use in a production application.

---

## Resizing an Image with resize()

```python
# Import the Image module from the PIL package
from PIL import Image

# Open the image file
img = Image.open("photo.jpg")

# Resize to exactly 600x500 pixels — returns a NEW image, does not change the original
resized_img = img.resize((600, 500))

# Save the new resized image to a file
resized_img.save("resized_photo.jpg")
```

The `.resize()` method takes a tuple of `(width, height)`, so the double parentheses are intentional — one pair for the tuple, one pair for the method call.

**Key point:** `.resize()` does **not** change the original image. It returns a **new** image object. That is why we store the result in `resized_img` and save it separately.

`.resize()` forces the image to the exact dimensions you specify, which can stretch or squash the image if the aspect ratio does not match.

---

## Resizing an Image with thumbnail()

```python
# Import the Image module from the PIL package
from PIL import Image

# Open the image file
img = Image.open("photo.jpg")

# Shrink the image to fit within 600x500 — modifies the image IN PLACE, no new image returned
img.thumbnail((600, 500))

# Save the modified image
img.save("thumbnail_photo.jpg")
```

There are two important differences between `.thumbnail()` and `.resize()`:

1. **In-place vs new image** — `.thumbnail()` modifies the image **in place**. It does not return a new image. There is no need to assign the result to a new variable.

2. **Aspect ratio** — `.thumbnail()` keeps the original aspect ratio. It shrinks the image so it fits *within* the size you specify, without distortion. The result might be 600x400 or 375x500, but never stretched or squashed.

This makes `.thumbnail()` the better choice when you want to scale down an image without it looking warped.

---

## Reading EXIF Data

```python
# Import the Image module from the PIL package
from PIL import Image

# Import TAGS — a dictionary that maps numeric EXIF tag IDs to readable names
from PIL.ExifTags import TAGS

# Open the image file
img = Image.open("photo.jpg")

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
```

`._getexif()` pulls the raw EXIF data from the image as a dictionary. The keys are numeric tag IDs like 271, 272, etc. Those numbers are not very readable, so we import `TAGS` from `PIL.ExifTags` — a lookup dictionary that maps the numeric IDs to human-friendly names like "Make", "Model", and "DateTime".

Not every image has EXIF data. Screenshots and images downloaded from the web often have it stripped out. Photos taken with a phone or camera are your best bet for seeing results.

---

## Reading Specific EXIF Tags

```python
# Import the Image module from the PIL package
from PIL import Image

# Import the TAGS dictionary for converting numeric IDs to readable names
from PIL.ExifTags import TAGS

# Open the image file
img = Image.open("large_assets/coffee_cup.jpg")

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
```

Here we created a **set** called `wanted_tags` containing only the tag names we care about. Inside the loop, we check if each tag name is in that set before printing it.

We use a set rather than a list because lookups in a set are faster. With a list, Python checks each item one by one. With a set, it jumps straight to the answer. For a small number of items the difference is negligible, but it is a good habit to build early.

---

## Writing EXIF Data

```python
# Import the Image module from the PIL package
from PIL import Image

# Import piexif — a separate library for writing EXIF data (pip install piexif)
import piexif

# Open the image file
img = Image.open("photo.jpg")

# Load existing EXIF data into a dictionary — if none exists, start with empty bytes
exif_dict = piexif.load(img.info.get("exif", b""))

# Add the Artist tag to the "0th" section (basic image info)
exif_dict["0th"][piexif.ImageIFD.Artist] = "Dele Oke"

# Add the ImageDescription tag to the "0th" section
exif_dict["0th"][piexif.ImageIFD.ImageDescription] = "A splendid cup of Coffee"

# Convert the dictionary back into raw bytes that can be embedded in an image
exif_bytes = piexif.dump(exif_dict)

# Save the image with the updated EXIF data
img.save("large_images/updated_photo.jpg", exif=exif_bytes)
```

Pillow can read EXIF data but cannot write or modify it. For that, we use the `piexif` library.

```bash
pip install piexif
```

Here is what each step does:

- `piexif.load()` reads the existing EXIF data into a dictionary structure
- We add or update fields by assigning values to specific tags
- `piexif.dump()` converts the dictionary back into raw bytes
- We pass those bytes into `.save()` using the `exif` parameter

EXIF data is organised into sections. `"0th"` covers basic image info like artist and description. `"Exif"` holds camera settings like shutter speed and ISO. `"GPS"` stores location coordinates.

---

## Key Takeaways

Before moving on, make sure you understand these core concepts:

- **`import PIL` vs `from PIL import Image`** — importing the PIL package alone does not load its sub-modules. Always import the specific module you need.
- **In-place vs new object** — some Pillow methods like `.thumbnail()` modify the image directly, while others like `.resize()` return a new image. Always check which pattern a method uses.
- **Tuples for dimensions** — methods like `.resize()` and `.thumbnail()` expect a tuple `(width, height)`, which is why you see double parentheses.
- **EXIF reading vs writing** — Pillow handles reading, but you need an additional library like `piexif` for writing.

---

## Practical Assignment

Choose **3 of your own photos** taken with a phone or camera (so they contain EXIF data) and write a Python script that does the following for each photo:

1. Opens the image and prints its width and height
2. Prints the camera model, date taken, and artist from the EXIF data (handle cases where a tag might be missing)
3. Creates a resized version at exactly 1200 x 800 pixels and saves it with the prefix `resized_`
4. Creates a thumbnail version that fits within 400 x 400 pixels and saves it with the prefix `thumb_`
5. Adds your name as the Artist in the EXIF data of the resized version

**Bonus challenge:** After creating both versions of each photo, print the file sizes of the original, resized, and thumbnail versions using the `os` library. Compare the results and note how dimensions affect file size.
