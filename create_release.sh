#!/bin/bash
# Script to create a new release

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}  Criar Release - Calculadora Integral${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""

# Get version
echo -e "${YELLOW}Digite a versão do release (ex: 1.0.0):${NC}"
read version

if [ -z "$version" ]; then
    echo "Versão não pode ser vazia!"
    exit 1
fi

# Confirm
echo ""
echo -e "${YELLOW}Você vai criar a versão: v${version}${NC}"
echo -e "${YELLOW}Isso vai:${NC}"
echo "  1. Criar uma tag git: v${version}"
echo "  2. Push para o GitHub"
echo "  3. Iniciar build automático"
echo "  4. Criar Release com executável"
echo ""
echo -e "${YELLOW}Continuar? (s/n):${NC}"
read confirm

if [ "$confirm" != "s" ] && [ "$confirm" != "S" ]; then
    echo "Cancelado."
    exit 0
fi

# Create tag
echo ""
echo -e "${GREEN}Criando tag v${version}...${NC}"
git tag -a "v${version}" -m "Release version ${version}"

if [ $? -ne 0 ]; then
    echo "Erro ao criar tag!"
    exit 1
fi

# Push tag
echo -e "${GREEN}Enviando tag para GitHub...${NC}"
git push origin "v${version}"

if [ $? -ne 0 ]; then
    echo "Erro ao enviar tag!"
    echo "Para reverter: git tag -d v${version}"
    exit 1
fi

echo ""
echo -e "${GREEN}========================================${NC}"
echo -e "${GREEN}✅ Release iniciado com sucesso!${NC}"
echo -e "${GREEN}========================================${NC}"
echo ""
echo "Aguarde 5-10 minutos para o build completar."
echo ""
echo "Acompanhe em:"
echo "  • Actions: https://github.com/VNaiff/Calculadora-integral-num/actions"
echo "  • Releases: https://github.com/VNaiff/Calculadora-integral-num/releases"
echo ""
echo -e "${GREEN}🎉 Pronto!${NC}"
