@echo off
setlocal

if not exist .venv py -3 -m venv .venv
call .venv\Scripts\activate

python -m pip install --upgrade pip
pip install -e .

cd voyager\env\mineflayer
call npm install -g npx
call npm install
cd mineflayer-collectblock
call npx tsc
cd ..
call npm install
cd ..\..\..

echo.
echo Voyager is ready.
echo Next: run python and call voyager.learn().
pause
