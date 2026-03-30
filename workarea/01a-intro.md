# Manipulation with Python Pillow on VS Code

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
[Open an Image](01-openImage.py)