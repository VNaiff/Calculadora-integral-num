# Calculadora com Integração Numérica

Uma calculadora moderna e modular com capacidades avançadas de integração numérica.

## Características

### Calculadora Básica
- Operações aritméticas básicas (+, -, *, /)
- Funções trigonométricas (sin, cos, tan)
- Funções logarítmicas (log, ln)
- Exponencial e potenciação
- Constantes matemáticas (π, e)
- Histórico de cálculos
- Interface gráfica moderna e intuitiva

### Integração Numérica
- **Múltiplos métodos de integração:**
  - Regra do Trapézio (Trapezoidal)
  - Regra de Simpson 1/3
  - Regra de Simpson 3/8
  - Método de Romberg
  - Método de Monte Carlo

- **Funcionalidades:**
  - Parser de expressões matemáticas
  - Visualização gráfica da função e área integrada
  - Estimativa de erro (quando aplicável)
  - Configuração do número de intervalos
  - Interface intuitiva separada por abas

## Instalação

### Pré-requisitos
- Python 3.8 ou superior

### Passos de Instalação

1. Clone o repositório:
```bash
git clone https://github.com/VNaiff/Calculadora-integral-num.git
cd Calculadora-integral-num
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Como Usar

### Iniciar a Aplicação

```bash
python main.py
```

### Usar a Calculadora Básica

1. Selecione a aba "Calculadora"
2. Digite a expressão usando os botões ou o teclado
3. Pressione "=" para calcular
4. O histórico é exibido na parte inferior

**Exemplos de expressões:**
- `2 + 2`
- `sin(pi/2)`
- `sqrt(16) + 3**2`
- `log10(100)`

### Calcular Integrais Numéricas

1. Selecione a aba "Integração Numérica"
2. Digite a função em termos de x (exemplo: `x**2`, `sin(x)`, `exp(-x**2)`)
3. Defina os limites de integração (a e b)
4. Escolha o número de intervalos (maior = mais preciso)
5. Selecione o método de integração
6. Clique em "Calcular Integral"

**Exemplos de funções:**
- `x**2` - função quadrática
- `sin(x)` - seno
- `exp(-x**2)` - gaussiana
- `1/x` - hipérbole
- `sqrt(1-x**2)` - semicírculo

### Visualizar Gráficos

Na aba de integração numérica, clique em "Plotar Função" para visualizar:
- O gráfico da função
- A área integrada (sombreada em verde)
- Os limites de integração (linhas vermelhas)

## Arquitetura do Projeto

O projeto foi desenvolvido com arquitetura modular para facilitar extensões futuras:

```
Calculadora-integral-num/
├── main.py                    # Ponto de entrada da aplicação
├── requirements.txt           # Dependências do projeto
├── README.md                  # Documentação
└── src/
    ├── __init__.py
    ├── core/                  # Lógica central da calculadora
    │   ├── __init__.py
    │   └── calculator.py      # Classe Calculator
    ├── integrators/           # Métodos de integração numérica
    │   ├── __init__.py
    │   └── numerical_integrator.py
    ├── gui/                   # Interface gráfica
    │   ├── __init__.py
    │   └── main_window.py     # Janela principal
    └── utils/                 # Utilidades e helpers
        └── __init__.py
```

## Adicionar Novas Funcionalidades

### Adicionar Novo Método de Integração

1. Abra `src/integrators/numerical_integrator.py`
2. Adicione o novo método ao enum `IntegrationMethod`
3. Implemente o método na classe `NumericalIntegrator`
4. O método será automaticamente disponibilizado na interface

**Exemplo:**
```python
class IntegrationMethod(Enum):
    # ... métodos existentes ...
    GAUSSIAN_QUADRATURE = "Gaussian Quadrature"

# Adicione o método na classe:
def _gaussian_quadrature(self, func, a, b, n):
    # Implementação aqui
    pass
```

### Adicionar Nova Operação à Calculadora

1. Abra `src/core/calculator.py`
2. Adicione a função ao dicionário `safe_dict` no método `evaluate()`
3. (Opcional) Adicione um botão na GUI em `src/gui/main_window.py`

## Métodos de Integração Numérica

### Regra do Trapézio
Aproxima a área sob a curva usando trapézios. Simples e rápido.
- **Erro:** O(h²)
- **Melhor para:** Funções lineares ou quase lineares

### Regra de Simpson 1/3
Usa parábolas para aproximar a curva. Mais preciso que trapézio.
- **Erro:** O(h⁴)
- **Melhor para:** Funções suaves

### Regra de Simpson 3/8
Variante de Simpson usando polinômios de terceiro grau.
- **Erro:** O(h⁴)
- **Melhor para:** Funções suaves

### Método de Romberg
Combina extrapolação de Richardson com regra do trapézio.
- **Erro:** Adaptativo, muito preciso
- **Melhor para:** Funções muito suaves, quando precisão é crítica

### Monte Carlo
Usa amostragem aleatória para estimar a integral.
- **Erro:** O(1/√n)
- **Melhor para:** Integrais de alta dimensão, funções complexas

## Tecnologias Utilizadas

- **Python 3.8+**
- **ttkbootstrap** - Interface gráfica moderna
- **NumPy** - Computação numérica
- **Matplotlib** - Visualização de gráficos
- **SymPy** - Manipulação simbólica (futuro)

## Funções Suportadas

### Funções Básicas
- `+, -, *, /` - Operações aritméticas
- `**` ou `^` - Potenciação
- `sqrt(x)` - Raiz quadrada
- `abs(x)` - Valor absoluto

### Funções Trigonométricas
- `sin(x)`, `cos(x)`, `tan(x)`
- `asin(x)`, `acos(x)`, `atan(x)`
- `sinh(x)`, `cosh(x)`, `tanh(x)`

### Funções Logarítmicas e Exponenciais
- `log(x)` ou `ln(x)` - Logaritmo natural
- `log10(x)` - Logaritmo base 10
- `exp(x)` - Exponencial (e^x)

### Constantes
- `pi` - π (3.14159...)
- `e` - Número de Euler (2.71828...)

## Exemplos de Uso

### Exemplo 1: Integrar x²
```
Função: x**2
Intervalo: [0, 1]
Método: Simpson
Resultado: 0.3333333333 (valor exato: 1/3)
```

### Exemplo 2: Integrar sin(x)
```
Função: sin(x)
Intervalo: [0, pi]
Método: Romberg
Resultado: 2.0000000000 (valor exato: 2)
```

### Exemplo 3: Gaussiana
```
Função: exp(-x**2)
Intervalo: [-3, 3]
Método: Simpson
Resultado: ≈ 1.7724 (√π)
```

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:
- Reportar bugs
- Sugerir novas funcionalidades
- Adicionar novos métodos de integração
- Melhorar a documentação

## Licença

Este projeto é de código aberto.

## Autor

Desenvolvido com Claude AI

## Contato

Para dúvidas ou sugestões, abra uma issue no GitHub.
