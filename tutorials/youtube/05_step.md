
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

[Next Page](06_step.md)
