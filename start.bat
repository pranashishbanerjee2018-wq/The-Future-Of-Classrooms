@echo off
title The Future of Classrooms - Academic Presentation & Simulation
cls
echo ===============================================================================
echo            THE FUTURE OF CLASSROOMS
echo    Reimagining Education Through Innovation, Intelligence and Technology
echo ===============================================================================
echo.

:: 1. Check Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERROR] Python is not found in your system PATH.
    echo Please install Python 3.9+ and add it to PATH.
    pause
    exit /b 1
)
echo [1/4] Python verified successfully.

:: 2. Verify / Generate Scientific Assets and Audio
echo [2/4] Verifying and generating scientific assets and audio...
python generate_assets.py
python generate_svgs.py
python build_index_html.py

:: 3. Launch Default Browser
echo [3/4] Launching default browser at http://127.0.0.1:5000/...
start http://127.0.0.1:5000/

:: 4. Start Flask Application Server
echo [4/4] Starting Flask Server...
echo Static alternative: Run 'python -m http.server 8000' and open http://127.0.0.1:8000/index.html
echo.
python app.py

pause
