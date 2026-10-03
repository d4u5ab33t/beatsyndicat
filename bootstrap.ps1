# Requires PowerShell
$ErrorActionPreference = "Stop"

$Root = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $Root

if (Test-Path (Join-Path $Root ".env.example")) {
    if (-not (Test-Path (Join-Path $Root ".env"))) {
        Copy-Item (Join-Path $Root ".env.example") (Join-Path $Root ".env")
    }
}

if (-not (Get-Command python -ErrorAction SilentlyContinue)) {
    throw "Python 3.10+ is required."
}

$venv = Join-Path $Root "venv"
if (-not (Test-Path $venv)) {
    & python -m venv $venv
}
. (Join-Path $venv "Scripts\Activate.ps1")
python -m pip install --upgrade pip setuptools wheel
if (Test-Path (Join-Path $Root "requirements.txt")) {
    python -m pip install -r (Join-Path $Root "requirements.txt")
}
python bootstrap.py --root $Root
python verify.py --root $Root
Write-Host "Bootstrap complete." -ForegroundColor Green
