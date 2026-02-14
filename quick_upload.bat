@echo off
echo ========================================
echo LogicLens AI - GitHub Upload Script
echo ========================================
echo.

echo Step 1: Checking for .env file...
if exist .env (
    echo [WARNING] .env file found! This should NOT be uploaded.
    echo Make sure .gitignore is working correctly.
    pause
) else (
    echo [OK] No .env file found in root.
)
echo.

echo Step 2: Initializing Git...
git init
echo.

echo Step 3: Adding files...
git add .
echo.

echo Step 4: Checking what will be committed...
echo [Files to be committed:]
git status
echo.

echo Step 5: Creating commit...
git commit -m "Initial commit: LogicLens AI - AI for Bharat Hackathon"
echo.

echo Step 6: Ready to push!
echo.
echo IMPORTANT: Replace YOUR_USERNAME with your GitHub username
echo Command: git remote add origin https://github.com/YOUR_USERNAME/LogicLens-AI.git
echo Then run: git push -u origin main
echo.

pause
