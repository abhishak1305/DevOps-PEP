1. Create a Virtual Environment

Creates an isolated Python environment named `venv`.

python -m venv venv


## 2. Activate the Virtual Environment

### On Windows (Command Prompt)

cmd
venv\Scripts\activate.bat

### On Windows (PowerShell)

venv\Scripts\Activate.ps1

### On Linux / macOS / Git Bash

source venv/scripts/activate


## 3. Fix PowerShell Execution Policy (if activation is blocked)

Set-ExecutionPolicy RemoteSigned -Scope CurrentUser

Check current execution policy:

powershell
Get-ExecutionPolicy


## 4. Save Installed Packages

Export all installed Python packages into a requirements file.

pip freeze > requirements.txt


## 5. Run a Python Script

python first.py

# Create virtual environment
python -m venv venv

# Activate environment
venv\Scripts\activate.bat   # CMD
venv\Scripts\Activate.ps1   # PowerShell

# Install packages
pip install package_name

# Save dependencies
pip freeze > requirements.txt

# Run project
python first.py

# Run requirements
pip install -r requirements.txt