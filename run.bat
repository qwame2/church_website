@echo off
echo Starting Django development server...

REM Check if manage.py exists
if not exist manage.py (
    echo Error: manage.py not found in the current directory.
    pause
    exit /b 1
)

REM Run the Django development server in the background
start python manage.py runserver

REM Wait for a few seconds to ensure the server is up
timeout /t 5 >nul

REM Open the browser with the Django development server URL
start http://127.0.0.1:8000/

echo Django development server is running. Press any key to stop...
pause

REM Stop the Django development server
taskkill /f /im python.exe