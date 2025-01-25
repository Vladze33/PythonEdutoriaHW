@REM cd homework_3
cd /d %~dp0

python -m venv .

call scripts\activate.bat
pip install --no-cache requests BeautifulSoup4