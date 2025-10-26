# 🚀 Guia de Deploy - Calculadora Web

Este guia mostra como hospedar a calculadora gratuitamente e compartilhar apenas um link.

## ⭐ Opção 1: Railway (MAIS FÁCIL - RECOMENDADO!)

**Tempo:** ~3 minutos | **Custo:** Gratuito | **Sem cartão de crédito**

### Passos:

1. **Acesse:** https://railway.app/

2. **Faça login com GitHub:**
   - Clique em "Login with GitHub"
   - Autorize o Railway

3. **Deploy do repositório:**
   - Clique em "New Project"
   - Selecione "Deploy from GitHub repo"
   - Escolha `Calculadora-integral-num`
   - Railway detectará automaticamente a configuração!

4. **Aguarde o build:**
   - O Railway vai instalar as dependências
   - Deploy automático (2-3 minutos)

5. **Obtenha o link público:**
   - Clique em "Settings" no seu projeto
   - Em "Networking", clique "Generate Domain"
   - **Pronto!** Copie o link: `https://seu-app.up.railway.app`

6. **Compartilhe com Paulo!** 🎉

### Vantagens:
✅ Mais fácil e rápido
✅ Deploy automático
✅ Sem cartão de crédito
✅ 500 horas grátis/mês
✅ HTTPS automático

---

## 🎨 Opção 2: Render

**Tempo:** ~5 minutos | **Custo:** Gratuito

### Passos:

1. **Acesse:** https://render.com/

2. **Faça login com GitHub**

3. **Novo Web Service:**
   - Clique em "New +" → "Web Service"
   - Conecte seu repositório GitHub
   - Selecione `Calculadora-integral-num`

4. **Configure:**
   - Name: `calculadora-integral`
   - Environment: `Python 3`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn webapp.app:app --host 0.0.0.0 --port $PORT`

5. **Deploy:**
   - Clique em "Create Web Service"
   - Aguarde 3-5 minutos

6. **Link gerado:**
   - `https://calculadora-integral.onrender.com`

### Vantagens:
✅ Gratuito permanente
✅ SSL/HTTPS incluído
✅ Auto-deploy no git push

### ⚠️ Observação:
- O plano gratuito "hiberna" após 15 min de inatividade
- Primeira requisição pode demorar 30s para "acordar"

---

## 🐳 Opção 3: Fly.io

**Tempo:** ~5 minutos | **Custo:** Gratuito

### Passos:

1. **Instale o Fly CLI:**
   ```bash
   # Mac/Linux
   curl -L https://fly.io/install.sh | sh

   # Windows (PowerShell)
   iwr https://fly.io/install.ps1 -useb | iex
   ```

2. **Login:**
   ```bash
   fly auth login
   ```

3. **Deploy:**
   ```bash
   cd Calculadora-integral-num
   fly launch
   ```
   - Aceite as configurações padrão
   - Aguarde o deploy

4. **Abra no navegador:**
   ```bash
   fly open
   ```

5. **Link gerado:**
   - `https://calculadora-integral.fly.dev`

### Vantagens:
✅ Muito rápido
✅ Não hiberna
✅ Excelente performance

---

## 🔥 Opção 4: Heroku

**Tempo:** ~5 minutos | **Requer cartão** (não cobra)

### Passos:

1. **Acesse:** https://heroku.com

2. **Instale Heroku CLI:**
   ```bash
   # Mac
   brew tap heroku/brew && brew install heroku

   # Windows
   # Baixe de: https://devcenter.heroku.com/articles/heroku-cli
   ```

3. **Login e deploy:**
   ```bash
   heroku login
   cd Calculadora-integral-num
   heroku create calculadora-integral-paulo
   git push heroku claude/numerical-integral-calculator-011CUUpbmokJ4QE5K74miVLr:main
   heroku open
   ```

4. **Link gerado:**
   - `https://calculadora-integral-paulo.herokuapp.com`

---

## 🌐 Opção 5: Ngrok (Temporário - Ideal para demonstração)

**Tempo:** ~2 minutos | **Custo:** Gratuito | **Temporário**

### Passos:

1. **Baixe ngrok:**
   - Acesse: https://ngrok.com/download
   - Crie conta gratuita
   - Baixe para seu sistema

2. **Inicie a aplicação:**
   ```bash
   cd Calculadora-integral-num
   python run_webapp.py
   ```

3. **Em outro terminal, inicie ngrok:**
   ```bash
   ngrok http 8000
   ```

4. **Copie o link público:**
   - Exemplo: `https://abc123.ngrok.io`
   - **Compartilhe com Paulo!**

### Vantagens:
✅ Mais rápido de todos
✅ Ótimo para demonstrações
✅ Não precisa fazer deploy

### ⚠️ Observação:
- Link expira quando você fecha o terminal
- Ideal para demonstração rápida

---

## 📊 Comparação Rápida

| Plataforma | Tempo | Permanente | Fácil | Recomendado |
|------------|-------|------------|-------|-------------|
| **Railway** | 3 min | ✅ Sim | ⭐⭐⭐⭐⭐ | ✅ **SIM** |
| **Render** | 5 min | ✅ Sim | ⭐⭐⭐⭐ | ✅ |
| **Fly.io** | 5 min | ✅ Sim | ⭐⭐⭐ | ✅ |
| **Ngrok** | 2 min | ❌ Não | ⭐⭐⭐⭐⭐ | Para demo |
| **Heroku** | 5 min | ✅ Sim | ⭐⭐⭐ | - |

---

## 🎯 Recomendação Final

### Para compartilhar com Paulo AGORA (demonstração):
👉 **Use Ngrok** - 2 minutos e está pronto!

### Para compartilhar permanentemente:
👉 **Use Railway** - Mais fácil, gratuito, sem cartão!

---

## 🆘 Precisa de Ajuda?

### Railway não está funcionando?
- Verifique se o repositório está no GitHub
- Certifique-se que o `railway.json` existe
- Verifique os logs no dashboard do Railway

### Render está lento?
- Normal! Plano gratuito hiberna após 15 min
- Primeiro acesso demora ~30s
- Considere usar Railway ou Fly.io

### Ngrok diz "Session Expired"?
- Link expira após ~2 horas no plano gratuito
- Crie conta no ngrok.com para links de 8h
- Ou use Railway para link permanente

---

## 📱 Testando o Deploy

Após o deploy, teste:

1. ✅ Acesse o link gerado
2. ✅ Teste a calculadora: `2 + 2 = 4`
3. ✅ Teste integração: `x**2` de 0 a 1 = 0.333...
4. ✅ Teste gráfico: Clique em "Plotar Função"
5. ✅ Compartilhe com Paulo! 🎉

---

## 💡 Dica Extra

Encurte o link para compartilhar:
- https://tinyurl.com/
- https://bit.ly/

Exemplo:
- Link original: `https://calculadora-integral-xyzabc.up.railway.app`
- Link curto: `https://bit.ly/calc-paulo`

---

## ✨ Pronto!

Agora você tem uma calculadora online profissional para compartilhar com o Paulo! 🚀
