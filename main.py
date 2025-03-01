import os
from pathlib import Path
import logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:%(message)s:')
# List of files we want to create
list_of_files = [
    ".vscode/settings.json",
    ".github/workflows/unittests.yml",
    ".gitignore",
    "requirements.txt",
    "README.md",
    "src/dashboard-div/app.py",
    "src/init.py",
    "notebooks/init.py",
    "notebooks/README.md",
    "tests/init.py",
    "scripts/init.py",
    "scripts/README.md"
]
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} is already created")