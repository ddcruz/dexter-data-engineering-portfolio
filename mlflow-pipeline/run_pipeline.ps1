$ErrorActionPreference = "Stop"

$python = ".venv\Scripts\python.exe"

if (-not (Test-Path $python)) {
    throw "Virtual environment not found at .venv. Create it first."
}

& $python notebooks\train.py
& $python notebooks\batch_inference.py

Write-Host "Pipeline completed: train then inference."
