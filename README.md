# How to Edit & Manipulate Images in Python with Pillow (VS Code & Colab)

Pillow is a Python library for opening, manipulating, and saving image files. It is a modern, maintained *fork* of the original **PIL** (Python Imaging Library), which is no longer actively developed.

## 1. What You Will Learn

This course begins with the fundamentals of image manipulation using the Pillow library — writing code by hand so you understand exactly what it does and why.

You'll then use AI tools to generate code for more complex tasks. Starting with the manual approach is essential: it gives you the foundation to critically evaluate and question what AI produces.

By the end, you'll be able to automate repetitive image tasks and confidently understand the code doing the work.

### Prerequisites

1. **VS Code** with the Python extension - `https://code.visualstudio.com/`
2. **Python 3.10+** installed on your system -`python.org`
3. **Git Bash** terminal (provides a consistent experience on both Mac and Windows) - `git-scm.com/`
4. VS Code Python Extension
5. Free Google account (gmail) - `Google Colab`

### Project Structure

```
project-root/
├── AGENTS.md          # AI agent instructions for code generation
├── README.md          # This file
├── .venv/*             # Python virtual environment
├── large_assets/      # Your source images (input)
├── large_images/      # Images produced by scripts (output)
├── tutorials/         # Tutorial documents
├── workarea/          # Python scripts
```

### Getting Started
1. Create a folder for this project - `pillow_Image_Introduction`
2. Create the folder structure (do not create .venv)
3. Download sample images  

```
- [large_image](https://pixabay.com/photos/street-walking-photography-urban-4846133/) 5806 X 1280
- [graffiti_dog](https://pixabay.com/photos/graffiti-dog-wall-artwork-urban-4389452/) 3397 X 3692
- [coffee_exif_image.jpg](https://creativewords.co.uk/students/delegate/coffee_exif_image.jpg)
```
Rename the images if necessary and save `large_image.jpg`, `graffiti_dog.jpg` and `coffee_exif_image.jpg`
into the `large_assets/` folder.


## Tutorials

- Tutorial documents are in the `tutorials/` folder. Work through them in order:
- Let us continue and I will show how to use `Google Colab` for the same examples as in the next lesson

---
### Introduction lesson
0. [Python Virtual Environmemt](tutorials/python_virtual_env.md)
0. [Introduction on VS Code](workarea/01a-intro.md)
1. [Open Image](workarea/01-openImage.py)
2. [Resize Image](workarea/01-resizeImage.py)
3. [Thumbnail](workarea/01-thumbnail.py)
4. [EXIF Data](workarea/01-exifData.py)
5. [EXIF Specific](workarea/01-exifSpecific.py)
6. [EXIF Writing](workarea/01-exifWriting.py)
7. [Compress Image](workarea/01-compressImage.py)
8. [Thumbnail EXIF](workarea/01-thumbnailExif.py)

---
## Useful Links

- [Pillow Documentation](https://pillow.readthedocs.io/)
- [Pillow on PyPI](https://pypi.org/project/Pillow/)
- [piexif Documentation](https://piexif.readthedocs.io/)
- [Python Documentation](https://docs.python.org/3/)
- [Venv - Python of Virtual Environments](https://docs.python.org/3/library/venv.html)
