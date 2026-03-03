from pathlib import Path

BAT_TEMPLATE = r"""@echo off
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
"""


def main() -> None:
    out = Path("install_voyager.bat")
    out.write_text(BAT_TEMPLATE, encoding="utf-8", newline="\r\n")
    print(f"Created {out.resolve()}")


if __name__ == "__main__":
    main()
