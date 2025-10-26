# Web App - Calculadora com Integração Numérica

Versão web da calculadora com interface moderna e responsiva.

## Iniciar o Servidor

### Linux/Mac
```bash
./run_webapp.sh
```

### Windows
```bash
run_webapp.bat
```

### Manual
```bash
python run_webapp.py
```

Acesse: **http://localhost:8000**

## Endpoints da API

### Calculadora
- `POST /api/calculate`
  ```json
  {
    "expression": "2 + 2"
  }
  ```

### Integração Numérica
- `POST /api/integrate`
  ```json
  {
    "function": "x**2",
    "lower_bound": 0,
    "upper_bound": 1,
    "method": "Simpson",
    "intervals": 1000
  }
  ```

### Outros
- `GET /api/methods` - Listar métodos disponíveis
- `GET /api/history` - Obter histórico
- `DELETE /api/history` - Limpar histórico
- `GET /health` - Status do servidor
- `GET /docs` - Documentação interativa (Swagger UI)

## Características

- ✨ Interface moderna e responsiva
- 📊 Gráficos interativos com Plotly.js
- 📱 Mobile-friendly
- 🚀 API RESTful completa
- 💾 Histórico persistente
- 🎨 Design moderno com gradientes

## Tecnologias

- **Backend:** FastAPI + Uvicorn
- **Frontend:** HTML5, CSS3, JavaScript ES6+
- **Gráficos:** Plotly.js
- **Estilo:** CSS3 com variáveis e gradientes

## Compartilhar

### Rede Local
1. Descubra seu IP: `ipconfig` (Windows) ou `ifconfig` (Linux/Mac)
2. Compartilhe: `http://SEU_IP:8000`

### Internet (ngrok)
```bash
ngrok http 8000
```

### Deploy em Cloud
Veja instruções no README principal.
