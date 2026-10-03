#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT_DIR"

printf '\n=== BeatSyndicat bootstrap ===\n'

if ! command -v python3 >/dev/null 2>&1; then
  echo "Python 3.10+ is required. Please install it first."
  exit 1
fi

PYTHON_BIN="$(command -v python3)"
VENV_DIR="$ROOT_DIR/venv"

if [ ! -d "$VENV_DIR" ]; then
  echo "Creating virtual environment at $VENV_DIR"
  "$PYTHON_BIN" -m venv "$VENV_DIR"
else
  echo "Using existing virtual environment at $VENV_DIR"
fi

# shellcheck source=/dev/null
source "$VENV_DIR/bin/activate"

python -m pip install --upgrade pip setuptools wheel
if [ -f requirements.txt ]; then
  python -m pip install -r requirements.txt
fi

mkdir -p config manifests agents database cache knowledge models logs output exports renders

python bootstrap.py --root "$ROOT_DIR"
python verify.py --root "$ROOT_DIR"

printf '\nSetup complete.\n'
printf 'Activate venv with: source %s/bin/activate\n' "$VENV_DIR"
printf 'Run app: python main.py --agent all --once\n\n' 
