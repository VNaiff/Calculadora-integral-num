#!/usr/bin/env python3
"""
Script to build Windows executable (.exe) using PyInstaller.
This creates a single .exe file that contains everything needed to run the calculator.
"""

import os
import sys
import shutil
import subprocess
from pathlib import Path

def clean_build_folders():
    """Remove previous build artifacts."""
    print("🧹 Limpando builds anteriores...")
    folders_to_remove = ['build', 'dist', '__pycache__']
    files_to_remove = ['*.spec']

    for folder in folders_to_remove:
        if os.path.exists(folder):
            shutil.rmtree(folder)
            print(f"   ✓ Removido: {folder}/")

    # Remove .spec files
    for spec_file in Path('.').glob('*.spec'):
        if spec_file.name != 'calculadora.spec':  # Keep our custom spec
            spec_file.unlink()
            print(f"   ✓ Removido: {spec_file}")

def check_pyinstaller():
    """Check if PyInstaller is installed."""
    try:
        import PyInstaller
        print("✓ PyInstaller instalado")
        return True
    except ImportError:
        print("❌ PyInstaller não encontrado!")
        print("   Instalando PyInstaller...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
        return True

def build_executable():
    """Build the executable using PyInstaller."""
    print("\n🔨 Construindo executável...")
    print("   Isso pode levar alguns minutos...\n")

    # PyInstaller command
    cmd = [
        'pyinstaller',
        '--name=Calculadora-Integral',
        '--onefile',
        '--windowed',
        '--icon=NONE',  # You can add an icon later
        '--add-data=src:src',
        '--hidden-import=ttkbootstrap',
        '--hidden-import=numpy',
        '--hidden-import=matplotlib',
        '--hidden-import=matplotlib.backends.backend_tkagg',
        '--hidden-import=PIL',
        '--hidden-import=PIL._tkinter_finder',
        '--collect-all=ttkbootstrap',
        '--collect-all=matplotlib',
        '--noconfirm',
        'main.py'
    ]

    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print("✅ Build concluído com sucesso!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro durante o build:")
        print(e.stderr)
        return False

def verify_executable():
    """Verify that the executable was created."""
    exe_path = Path('dist/Calculadora-Integral.exe')

    if exe_path.exists():
        size_mb = exe_path.stat().st_size / (1024 * 1024)
        print(f"\n✅ Executável criado com sucesso!")
        print(f"   📁 Local: {exe_path.absolute()}")
        print(f"   📊 Tamanho: {size_mb:.1f} MB")
        return True
    else:
        print(f"\n❌ Executável não encontrado em: {exe_path}")
        return False

def create_readme():
    """Create a README for the release."""
    readme_content = """# Calculadora com Integração Numérica - Executável Windows

## Download

Baixe o arquivo `Calculadora-Integral.exe`

## Como Usar

1. **Baixe** o arquivo `Calculadora-Integral.exe`
2. **Execute** o arquivo (duplo clique)
3. Se o Windows Smart Screen aparecer:
   - Clique em "Mais informações"
   - Clique em "Executar assim mesmo"

## Funcionalidades

- ✅ Calculadora básica completa
- ✅ Funções matemáticas avançadas
- ✅ Integração numérica com 5 métodos
- ✅ Visualização gráfica
- ✅ Interface moderna

## Métodos de Integração

- Regra do Trapézio
- Regra de Simpson 1/3
- Regra de Simpson 3/8
- Método de Romberg
- Método de Monte Carlo

## Requisitos

- Windows 10 ou superior
- Nenhuma instalação adicional necessária!

## Observações

- Arquivo único, portátil
- Não requer Python instalado
- Primeira execução pode ser lenta (Windows verifica o arquivo)

## Problemas?

Se o antivírus bloquear:
1. É um falso positivo (comum com executáveis PyInstaller)
2. Adicione uma exceção no seu antivírus
3. Ou compile você mesmo usando o código fonte

## Código Fonte

Disponível em: https://github.com/VNaiff/Calculadora-integral-num
"""

    readme_path = Path('dist/README.txt')
    readme_path.write_text(readme_content, encoding='utf-8')
    print(f"   📝 README criado: {readme_path}")

def main():
    """Main build process."""
    print("=" * 60)
    print("🧮 CALCULADORA COM INTEGRAÇÃO NUMÉRICA")
    print("   Build de Executável Windows (.exe)")
    print("=" * 60)
    print()

    # Check Python version
    if sys.version_info < (3, 8):
        print("❌ Python 3.8+ necessário!")
        sys.exit(1)

    print(f"✓ Python {sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}")

    # Check PyInstaller
    if not check_pyinstaller():
        sys.exit(1)

    # Clean previous builds
    clean_build_folders()

    # Build executable
    if not build_executable():
        print("\n❌ Build falhou!")
        sys.exit(1)

    # Verify executable
    if not verify_executable():
        sys.exit(1)

    # Create README
    create_readme()

    print("\n" + "=" * 60)
    print("✨ SUCESSO!")
    print("=" * 60)
    print("\n📦 Arquivos para distribuição:")
    print(f"   - dist/Calculadora-Integral.exe")
    print(f"   - dist/README.txt")
    print("\n💡 Próximos passos:")
    print("   1. Teste o executável: dist/Calculadora-Integral.exe")
    print("   2. Crie um Release no GitHub")
    print("   3. Faça upload dos arquivos da pasta dist/")
    print("\n🎉 Pronto para distribuir!\n")

if __name__ == "__main__":
    main()
