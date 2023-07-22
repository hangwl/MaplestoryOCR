@echo off
setlocal

set VENV_NAME=.venv

if not exist %VENV_NAME% (
    echo Virtual environment '%VENV_NAME%' not found. Please run setup.bat and create the virtual environment first.
    exit /b 1
)

REM Activate the virtual environment.
call %VENV_NAME%\Scripts\activate

REM Run the Python script.
python scripts\get_contributions.py

REM Deactivate the virtual environment.
deactivate

echo Script execution completed.
exit /b 0
