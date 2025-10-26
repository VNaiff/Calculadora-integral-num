@echo off
REM Script to create a new release on Windows

echo ========================================
echo   Criar Release - Calculadora Integral
echo ========================================
echo.

REM Get version
set /p version="Digite a versao do release (ex: 1.0.0): "

if "%version%"=="" (
    echo Versao nao pode ser vazia!
    pause
    exit /b 1
)

REM Confirm
echo.
echo Voce vai criar a versao: v%version%
echo Isso vai:
echo   1. Criar uma tag git: v%version%
echo   2. Push para o GitHub
echo   3. Iniciar build automatico
echo   4. Criar Release com executavel
echo.
set /p confirm="Continuar? (s/n): "

if /i not "%confirm%"=="s" (
    echo Cancelado.
    pause
    exit /b 0
)

REM Create tag
echo.
echo Criando tag v%version%...
git tag -a "v%version%" -m "Release version %version%"

if errorlevel 1 (
    echo Erro ao criar tag!
    pause
    exit /b 1
)

REM Push tag
echo Enviando tag para GitHub...
git push origin "v%version%"

if errorlevel 1 (
    echo Erro ao enviar tag!
    echo Para reverter: git tag -d v%version%
    pause
    exit /b 1
)

echo.
echo ========================================
echo Sucesso! Release iniciado!
echo ========================================
echo.
echo Aguarde 5-10 minutos para o build completar.
echo.
echo Acompanhe em:
echo   - Actions: https://github.com/VNaiff/Calculadora-integral-num/actions
echo   - Releases: https://github.com/VNaiff/Calculadora-integral-num/releases
echo.
echo Pronto!
pause
