# How to Edit & Manipulate Images in Python with Pillow (VS Code & Colab)

Pillow is a Python library for opening, manipulating, and saving image files. It is a modern, maintained *fork* of the original **PIL** (Python Imaging Library), which is no longer actively developed.

## What You Will Learn

This course begins with the fundamentals of image manipulation using the Pillow library — writing code by hand so you understand exactly what it does and why.

You'll then use AI tools to generate code for more complex tasks. Starting with the manual approach is essential: it gives you the foundation to critically evaluate and question what AI produces.

By the end, you'll be able to automate repetitive image tasks and confidently understand the code doing the work.

## Prerequisites

1. **VS Code** with the Python extension - `https://code.visualstudio.com/`
2. **Python 3.10+** installed on your system -`python.org`
3. **Git Bash** terminal (provides a consistent experience on both Mac and Windows) - `git-scm.com/`
4. VS Code Python Extension
5. Free Google account (gmail) - `Google Colab`

## Project Structure

```
project-root/
├── AGENTS.md          # AI agent instructions for code generation
├── README.md          # This file
├── venv/*             # Python virtual environment
├── large_assets/      # Your source images (input)
├── large_images/      # Images produced by scripts (output)
├── tutorials/         # Tutorial documents
├── workarea/          # Python scripts
```

## Getting Started
1. Create a folder for this project - `pillow_Image_Introduction`
2. Create the folder structure (do not create venv)
3. Download sample images  

```
- [large_image](https://pixabay.com/photos/street-walking-photography-urban-4846133/) 5806 X 1280
- [graffiti_dog](https://pixabay.com/photos/graffiti-dog-wall-artwork-urban-4389452/) 3397 X 3692
```

4. Create a repository
Open a **git bash** terminal in the project root folder and follow these steps.

```bash
git init
```

**2. Create and activate a virtual environment**

```bash
# active the VE on  Git Bash
python -m venv venv
source venv/Scripts/activate # windows
source .venv/bin/activate    # Mac
```

**3. Install dependencies**

```bash
# Install pillow and check
pip install pillow
pip list
which python
```

**4. Add your photos**

Copy a few of your own JPEG photos into the `large_assets/` folder. These will be used throughout the tutorials and assignments.

**5. Open the project in VS Code**

Make sure VS Code is using the Python interpreter from your `venv/` folder. You can check this in the bottom status bar or by opening the command palette and selecting **Python: Select Interpreter**.

```bash
# check where python is running using Git Bash
which python

# Save installations to requirements.txt
pip freeze > requirements.txt

# deactivate VE when finished
deactivate

# activate
```

**deleteing a Venv**

## Running Scripts

All Python scripts live in the `workarea/` folder. To run a script, make sure your virtual environment is activated, then:

Output images will be saved to the `large_images/` folder.

## Tutorials

- Tutorial documents are in the `tutorials/` folder. Work through them in order:
- Let us continue and I will show how to use `Google Colab` for the same examples as in the next lesson

---
### Introduction lesson

1. [Introduction on VS Code](workarea/01a-intro.md)



---
## Useful Links

- [Pillow Documentation](https://pillow.readthedocs.io/)
- [Pillow on PyPI](https://pypi.org/project/Pillow/)
- [piexif Documentation](https://piexif.readthedocs.io/)
- [Python Documentation](https://docs.python.org/3/)
