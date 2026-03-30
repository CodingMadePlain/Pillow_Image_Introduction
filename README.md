# Python Pillow for Photographers

A beginner-friendly on Python Pillow and how to manipulate images. 

No prior programming experience is required.

## What You Will Learn

This course starts with the fundamentals of image manipulation using the Pillow library, how to write code by hand and understand the syntax and workings of the code. 

We then move on to using AI tools to generate code for more complex tasks.
The first lesson is essential is it gives you an understanding of how to write the code yourself, this should equip you to be able to assess and query the code that AI generates later on in the course.

 By the end, you will be able to automate repetitive image tasks that currently eat into your editing time, and still eunderstand what code is being gegenerated for you..

**Part 1 — Understanding the Code**

- Opening images and reading their properties
- Resizing images with `resize()` and `thumbnail()` and understanding when to use each
- Reading, filtering, and writing EXIF metadata
- Key Python patterns you need to recognise when working with AI-generated code

**Part 2 — Working with AI**

- Batch processing and renaming files
- Watermarking
- Image adjustments (brightness, contrast, sharpness, colour balance)
- Format conversion
- Contact sheets
- Image comparison
- Colour analysis
- Social media templates
- PDF portfolio creation

## Prerequisites

- **Python 3.10+** installed on your system
- **VS Code** with the Python extension
- **Git Bash** terminal (provides a consistent experience on both Mac and Windows)
- A few of your own photos taken with a phone or camera (JPEG format with EXIF data)

## Project Structure

```
project-root/
├── AGENTS.md          # AI agent instructions for code generation
├── README.md          # This file
├── venv/              # Python virtual environment
├── large_assets/      # Your source images (input)
├── large_images/      # Images produced by scripts (output)
├── tutorials/         # Tutorial documents
├── workarea/          # Python scripts
```

## Getting Started

Open a **git bash** terminal in the project root folder and follow these steps.

**1. Create the folder structure**

```bash
mkdir large_assets large_images tutorials workarea
```

**2. Create and activate a virtual environment**

```bash
python -m venv venv
source venv/Scripts/activate
```

**3. Install dependencies**

```bash
pip install pillow piexif numpy
```

**4. Add your photos**

Copy a few of your own JPEG photos into the `large_assets/` folder. These will be used throughout the tutorials and assignments.

**5. Open the project in VS Code**

```bash
code .
```

Make sure VS Code is using the Python interpreter from your `venv/` folder. You can check this in the bottom status bar or by opening the command palette and selecting **Python: Select Interpreter**.

## Running Scripts

All Python scripts live in the `workarea/` folder. To run a script, make sure your virtual environment is activated, then:

```bash
cd workarea
python script_name.py
```

Output images will be saved to the `large_images/` folder.

## Tutorials

Tutorial documents are in the `tutorials/` folder. Work through them in order:

1. **pillow-tutorial-01-image-basics.md** — Opening images, dimensions, resizing, EXIF data

More tutorials will be added as the course progresses.

## Useful Links

- [Pillow Documentation](https://pillow.readthedocs.io/)
- [Pillow on PyPI](https://pypi.org/project/Pillow/)
- [piexif Documentation](https://piexif.readthedocs.io/)
- [Python Documentation](https://docs.python.org/3/)
