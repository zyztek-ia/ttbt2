@echo off
echo Instalando dependencias...
pip install -r requirements.txt
pip install pyinstaller

echo Creando el ejecutable...
pyinstaller --onefile --add-data "accounts.json;." --add-data "fingerprints\fingerprints.json;fingerprints" --add-data "proxies\proxies.json;proxies" main.py

echo.
echo Proceso completado. El ejecutable se encuentra en la carpeta 'dist'.
pause
