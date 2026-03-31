# AGENTS.md

## Project Overview

This is a **Python Pillow tutorial** designed for **beginners**. The delegates are learning how to manipulate images with Python. Many have no prior programming experience. All code and explanations must reflect this.

## Code Style

- Write **simple, readable code** that a beginner can follow line by line
- Use **clear variable names** that describe what they hold (e.g. `resized_img` not `r_img`)
- Add **comments to explain why**, not just what. Do not over-comment obvious lines
- Keep scripts short and focused on one concept at a time
- Avoid advanced Python features such as list comprehensions, decorators, generators, lambda functions, or ternary expressions unless explicitly requested
- Use `print()` statements to show progress and results so students can see what the code is doing
- When a Pillow method modifies the image **in place** (e.g. `.thumbnail()`), add a comment noting this. When a method returns a **new image** (e.g. `.resize()`), note that too. This distinction is a key learning point throughout the course

## Python Environment

- Always use a **virtual environment** (venv)
- The venv is located in the project root as `.venv/`
- To create the venv: `python -m venv .venv`
- To activate in git bash: `source .venv/Scripts/activate`
- Install dependencies with: `pip install pillow piexif numpy`
- The preferred terminal is **git bash**, which provides a consistent experience across Mac and Windows
- When giving terminal commands, use **git bash syntax** (forward slashes for paths, `source` for activation)

## Folder Structure

All paths are relative to the project root.

```
project-root/
├── AGENTS.md
├── .venv/
├── large_assets/      # Source images for examples and assignments (input)
├── large_images/      # Images produced by AI-generated scripts (output)
├── tutorials/         # Tutorial documents and markdown files
├── workarea/          # All Python scripts go here
```

- **large_assets/** — Contains all source images used in examples and assignments. Always read images from this folder. Never modify or overwrite files in this folder.
- **large_images/** — All images created or saved by scripts go here. This is the output folder.
- **tutorials/** — Tutorial documents, markdown files, and reference materials.
- **workarea/** — All Python scripts generated must be saved here.

## File Paths in Code

When writing scripts that are run from the `workarea/` folder, use relative paths that go up one level to reach the project root folders:

```python
# Reading a source image
img = Image.open("../large_assets/large_image.jpg")

# Saving an output image
img.save("../large_images/resized_image.jpg")
```

If a script is run from the project root instead, adjust accordingly. Add a comment at the top of each script indicating the expected working directory.

## Script Header

Every Python script should begin with a brief comment block:

```python
# Script: script_name.py
# Topic: Brief description of what this script demonstrates
# Run from: workarea/
```

## Generating Tutorials

- Save tutorial documents to the `tutorials/` folder
- Use markdown format
- Keep explanations concise and suitable for classroom or video delivery

## General Rules

- Do not assume students have any prior Python knowledge beyond basic syntax
- When introducing a new Pillow method or module, briefly explain what it does before using it
- Always use `from PIL import Image` (and other specific imports) rather than `import PIL`
- Handle potential errors gracefully with simple checks (e.g. verify EXIF data exists before looping through it)
- When a script requires an additional package beyond Pillow, mention the install command in a comment at the top of the script
