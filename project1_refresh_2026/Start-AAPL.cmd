@echo off
setlocal
cd /d "%~dp0"
echo Open http://127.0.0.1:8766 after the server starts. Ctrl+C stops it.
if exist "%USERPROFILE%\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe" (
 "%USERPROFILE%\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe" run.py --serve --port 8766
) else (
 python run.py --serve --port 8766
)
pause
