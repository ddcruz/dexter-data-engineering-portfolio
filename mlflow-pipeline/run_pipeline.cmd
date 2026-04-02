@echo off
setlocal

set "PYTHON=.venv\Scripts\python.exe"

if not exist "%PYTHON%" (
  echo Virtual environment not found at .venv
  echo Create it first, then install requirements.
  exit /b 1
)

echo Running training step...
"%PYTHON%" notebooks\train.py
if errorlevel 1 exit /b %errorlevel%

echo Running batch inference step...
"%PYTHON%" notebooks\batch_inference.py
if errorlevel 1 exit /b %errorlevel%

echo Pipeline completed: train then inference.
exit /b 0
