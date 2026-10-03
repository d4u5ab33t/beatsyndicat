#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$ROOT_DIR"

if [ -f .env.example ] && [ ! -f .env ]; then
  cp .env.example .env
fi

python3 -m venv venv || python -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements.txt
python bootstrap.py --root "$ROOT_DIR"
python verify.py --root "$ROOT_DIR"
