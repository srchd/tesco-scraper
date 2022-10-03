@echo off
set NEEDED_ENV=tesco-scrap
call update_environment.bat
call conda activate %NEEDED_ENV%
if %errorlevel% neq 0 exit /b %errorlevel%
call py startVSCode.py
@echo on