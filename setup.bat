@echo off
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Python is not installed. Please install it and try again.
    exit /b 1
)

python one_click_app.py
pause
