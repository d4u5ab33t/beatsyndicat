# Requires PowerShell 5.1+
$ErrorActionPreference = "Stop"

$Root = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $Root

Write-Host "=== BeatSyndicat bootstrap ===" -ForegroundColor Cyan

$python = Get-Command python -ErrorAction SilentlyContinue
if (-not $python) {
    throw "Python 3.10+ is required and not found in PATH."
}

$VenvDir = Join-Path $Root "venv"
if (-not (Test-Path $VenvDir)) {
    Write-Host "Creating virtual environment at $VenvDir" -ForegroundColor Yellow
    & $python.Source -m venv $VenvDir
} else {
    Write-Host "Using existing venv at $VenvDir" -ForegroundColor Yellow
}

$ActivateScript = Join-Path $VenvDir "Scripts\Activate.ps1"
if (-not (Test-Path $ActivateScript)) {
    throw "Virtual environment activation script not found: $ActivateScript"
}
. $ActivateScript

python -m pip install --upgrade pip setuptools wheel
if (Test-Path (Join-Path $Root "requirements.txt")) {
    python -m pip install -r (Join-Path $Root "requirements.txt")
}

$dirs = @("config", "manifests", "agents", "database", "cache", "knowledge", "models", "logs", "output", "exports", "renders")
foreach ($dir in $dirs) {
    $path = Join-Path $Root $dir
    if (-not (Test-Path $path)) {
        New-Item -ItemType Directory -Path $path -Force | Out-Null
    }
}

python bootstrap.py --root $Root
python verify.py --root $Root

Write-Host "\nSetup complete." -ForegroundColor Green
Write-Host "Activate the venv with: .\venv\Scripts\Activate.ps1" -ForegroundColor Cyan
Write-Host "Run the app with: python main.py --agent all --once" -ForegroundColor Cyan
