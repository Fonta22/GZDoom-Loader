@echo off

if "%1" == "" (
    echo You need to specify a WAD file as argument.
    exit
)

:: Delete currently used WAD
del .\*.WAD

:: Load WAD
echo.
echo Loading %1.WAD
copy .\WAD\%1.WAD .
echo.

:: Start GZDoom
start .\gzdoom.exe
if errorlevel 1 echo. & exit

:: Check Discord flag was specified
if not "%2" == "-dsc" exit

:: Install Python dependencies
pip install pypresence psutil python-dotenv --quiet

:: Start Discord Presence with Python
::echo.
python presence.py %1