# Python Virtual Environment 

- How to Create & Activate
*By Dele Oke*



---
## 1. What is a Python Virtual Environment

A Python virtual environment is a separate, isolated space on your computer where you can install Python packages for a specific project, without affecting the packages installed in your main Python setup.

---
When you install Python it comes with a built-in `venv` (Virtual Environment) that is built in. This is what we shall explore here.

There are several other third-party options such as `virtualenv`, `Conda`, `Poetry`, `Pipenv`

---
The `venv` Python module supports creating lightweight “virtual environments”, each with their own independent set of Python packages installed in their site directories. 

`venv` are completely self-contained. No settings get written to some hidden registry, no system files get modified. Everything lives inside that one folder, so deleting the folder is a clean removal.
---

## 2. Prerequisites

I will be using Visual Studio Code (VS Code) as my IDE to set up the Python `venv` on Windows 11. 
I will be using Git Bash through the VS Code terminal.
This set-up will also work perfectly on a MacOS.

Have the following installed

1. **VS Code** with the Python extension - `https://code.visualstudio.com/`
2. **Python 3.10+** installed on your system -`python.org`
3. **Git Bash** terminal (provides a consistent experience on both Mac and Windows) - `git-scm.com/`
4. VS Code Python Extension
---


## 3. Create & Activate one

We shall be using [Git Bash](https://git-scm.com/) - `git-scm.com`

```bash
# active the VE on  Git Bash
python -m venv .venv
```


```bash
source .venv/bin/activate   # activate it (Mac/Linux)
source .venv/Scripts/activate      # activate it (Windows)

## Check activation worked
which python
```

## 4. Install dependencies
These will no go inside your `venv`

```bash
# Install pillow and check
pip install pillow

## Check dependencies installed
pip list

# when done
deactivate

# Save your packages for easy reinstall
pip freeze > requirements.txt

# Install from requirements
pip install -r requirements.txt 

# close the venv
deactivate

# Delete the venv (Only when you no longer require it)
rm -rf .venv
```
---




## 5. Running scripts on Virtual Environment

- Convert jpg to png and resize with thumbnail
    [01 convertThumb.py](../workarea/01-convertThumbnail.py)

---

## 6. Conclusion