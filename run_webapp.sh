#!/bin/bash

# Script to run the web application on Linux/Mac

echo "===================================================="
echo "Calculadora com Integração Numérica - Web App"
echo "===================================================="
echo ""
echo "Instalando dependências..."
pip install -r requirements.txt

echo ""
echo "Iniciando servidor..."
echo ""
echo "Acesse: http://localhost:8000"
echo "Pressione CTRL+C para parar"
echo ""
echo "===================================================="

python3 run_webapp.py
