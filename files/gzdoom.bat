@echo off

:: Delete currently used WAD
del .\*.WAD

:: Load WAD
echo.
echo Loading %1.WAD
copy .\WAD\%1.WAD .

:: Start GZDoom
start .\gzdoom.exe

:: Start Discord Presence with Python
echo.
python presence.py %1