# BeatSyndicat package bootstrap helpers

This repository includes:

- bootstrap.py for directory/database bootstrap
- setup.sh and setup.ps1 for environment setup
- verify.py to confirm structure and key files
- main.py as the entry point

Troubleshooting:

1. If Python is missing, install Python 3.10+ and rerun the setup script.
2. If pip install fails due to system libraries, create a venv and install inside it.
3. If verify.py reports missing directories, run: python bootstrap.py --root .
4. If a dependency fails to install, run: python -m pip install --upgrade pip setuptools wheel
5. If you are on Windows, use PowerShell and run: .\setup.ps1
6. If you are on Linux/macOS, run: bash setup.sh
