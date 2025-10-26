# 🔨 Como Criar o Executável (.exe)

Este guia mostra como criar um executável Windows standalone da calculadora.

---

## 🎯 Opção 1: Automático via GitHub Actions (RECOMENDADO)

### Criar Release Automaticamente

1. **Faça commit e push das alterações:**
   ```bash
   git add .
   git commit -m "Preparar release"
   git push
   ```

2. **Crie uma tag de versão:**
   ```bash
   # Exemplo para versão 1.0.0
   git tag v1.0.0
   git push origin v1.0.0
   ```

3. **Aguarde o build:**
   - Acesse: `https://github.com/VNaiff/Calculadora-integral-num/actions`
   - O GitHub Actions vai:
     - ✅ Instalar dependências
     - ✅ Construir o executável
     - ✅ Criar um Release automático
     - ✅ Fazer upload do .exe

4. **Download do Release:**
   - Acesse: `https://github.com/VNaiff/Calculadora-integral-num/releases`
   - Baixe `Calculadora-Integral.exe`

### Vantagens:
- ✅ Totalmente automático
- ✅ Build em ambiente limpo
- ✅ Release criado automaticamente
- ✅ Não precisa de ambiente Windows local

---

## 💻 Opção 2: Build Local (Manual)

### Requisitos:
- Windows 10 ou superior
- Python 3.8+
- Git (opcional)

### Passos:

#### 1. Instalar dependências
```bash
pip install -r requirements.txt
```

#### 2. Executar script de build
```bash
python build_exe.py
```

O script vai:
- ✅ Verificar PyInstaller
- ✅ Limpar builds anteriores
- ✅ Criar o executável
- ✅ Gerar README

#### 3. Localizar o executável
```
dist/
├── Calculadora-Integral.exe  ← Executável
└── README.txt                ← Instruções
```

#### 4. Testar
```bash
# Execute o .exe
dist\Calculadora-Integral.exe
```

---

## 🛠️ Opção 3: Build Manual com PyInstaller

### Comando direto:
```bash
pyinstaller --name=Calculadora-Integral ^
            --onefile ^
            --windowed ^
            --add-data=src:src ^
            --hidden-import=ttkbootstrap ^
            --hidden-import=numpy ^
            --hidden-import=matplotlib ^
            --collect-all=ttkbootstrap ^
            --noconfirm ^
            main.py
```

### Usando o arquivo spec:
```bash
pyinstaller calculadora.spec
```

---

## 📦 Criar Release no GitHub (Manual)

Se você construiu localmente e quer criar um release:

### 1. Acesse Releases
```
https://github.com/VNaiff/Calculadora-integral-num/releases
```

### 2. Criar novo Release
- Clique em "Create a new release"
- Tag: `v1.0.0` (ou sua versão)
- Title: `Calculadora Integral v1.0.0`

### 3. Upload dos arquivos
Arraste e solte:
- `dist/Calculadora-Integral.exe`
- `dist/README.txt`

### 4. Descrição do Release
```markdown
## Calculadora com Integração Numérica

Download do executável Windows standalone.

### Como usar:
1. Baixe `Calculadora-Integral.exe`
2. Execute o arquivo (duplo clique)
3. Se aparecer aviso do Windows, clique "Executar assim mesmo"

### Funcionalidades:
- Calculadora básica completa
- Funções matemáticas avançadas
- 5 métodos de integração numérica
- Visualização gráfica

### Requisitos:
- Windows 10+
- Nenhuma instalação adicional necessária
```

### 5. Publicar
- Marque: "Set as the latest release"
- Clique em "Publish release"

---

## 🔍 Troubleshooting

### Erro: "PyInstaller não encontrado"
```bash
pip install pyinstaller
```

### Erro: "ModuleNotFoundError"
```bash
# Reinstale todas as dependências
pip install -r requirements.txt --force-reinstall
```

### Executável muito grande
Normal! O executável inclui:
- Python interpreter
- NumPy, Matplotlib, ttkbootstrap
- Todas as bibliotecas necessárias
- Tamanho esperado: 50-100 MB

### Windows Smart Screen bloqueia
1. Isso é normal para executáveis não assinados
2. Clique em "Mais informações"
3. Clique em "Executar assim mesmo"
4. Para produção, considere assinar o executável

### Antivírus bloqueia
1. Falso positivo comum com PyInstaller
2. Adicione exceção no antivírus
3. Ou compile você mesmo para confiar

---

## 📋 Checklist de Release

Antes de criar um release:

- [ ] Testar aplicação localmente (`python main.py`)
- [ ] Atualizar versão no código se necessário
- [ ] Fazer commit de todas as mudanças
- [ ] Criar tag de versão (`git tag v1.0.0`)
- [ ] Push da tag (`git push origin v1.0.0`)
- [ ] Aguardar GitHub Actions build
- [ ] Testar executável baixado do release
- [ ] Verificar README.txt no release

---

## 🎯 Resumo Rápido

### Para criar release automático:
```bash
git tag v1.0.0
git push origin v1.0.0
```
Aguarde 5-10 minutos. Pronto!

### Para build local:
```bash
python build_exe.py
```
Executável em: `dist/Calculadora-Integral.exe`

---

## 🚀 Versões Futuras

Para criar novas versões:

### v1.0.1 (patch - bugfix)
```bash
git tag v1.0.1
git push origin v1.0.1
```

### v1.1.0 (minor - nova funcionalidade)
```bash
git tag v1.1.0
git push origin v1.1.0
```

### v2.0.0 (major - mudanças grandes)
```bash
git tag v2.0.0
git push origin v2.0.0
```

---

## 💡 Dicas

### Reduzir tamanho do executável:
1. Use `--exclude-module` para módulos não usados
2. Desative UPX: `upx=False` no spec
3. Considere criar instalador ao invés de executável único

### Adicionar ícone:
1. Crie/baixe um arquivo `.ico`
2. Edite `calculadora.spec`:
   ```python
   icon='caminho/para/icon.ico'
   ```

### Incluir arquivos extras:
Edite `calculadora.spec`, seção `datas`:
```python
datas=[
    ('src', 'src'),
    ('images', 'images'),  # adicione aqui
],
```

---

## 📚 Referências

- PyInstaller: https://pyinstaller.org/
- GitHub Actions: https://docs.github.com/actions
- Semantic Versioning: https://semver.org/

---

## ✨ Pronto!

Agora você pode criar executáveis Windows facilmente e distribuir sua calculadora! 🎉
