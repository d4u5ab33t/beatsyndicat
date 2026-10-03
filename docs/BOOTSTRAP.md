# BeatSyndicat bootstrap guide

## Prerequisites

- Python 3.10+
- pip
- Git

## Setup on Linux/macOS

```bash
bash setup.sh
```

## Setup on Windows PowerShell

```powershell
.\setup.ps1
```

## Manual setup

```bash
python3 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements.txt
python bootstrap.py --root .
python verify.py --root .
```

## Run the app

```bash
python main.py --agent all --once
```
