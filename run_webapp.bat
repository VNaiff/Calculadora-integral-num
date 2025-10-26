@echo off

REM Script to run the web application on Windows

echo ====================================================
echo Calculadora com Integracao Numerica - Web App
echo ====================================================
echo.
echo Instalando dependencias...
pip install -r requirements.txt

echo.
echo Iniciando servidor...
echo.
echo Acesse: http://localhost:8000
echo Pressione CTRL+C para parar
echo.
echo ====================================================

python run_webapp.py
pause
