// Global state
let currentExpression = '';

// Tab Management
function openTab(event, tabName) {
    // Hide all tab contents
    const tabContents = document.getElementsByClassName('tab-content');
    for (let content of tabContents) {
        content.classList.remove('active');
    }

    // Remove active class from all buttons
    const tabButtons = document.getElementsByClassName('tab-button');
    for (let button of tabButtons) {
        button.classList.remove('active');
    }

    // Show selected tab and mark button as active
    document.getElementById(tabName).classList.add('active');
    event.currentTarget.classList.add('active');
}

// Calculator Functions
function appendToDisplay(value) {
    currentExpression += value;
    document.getElementById('calc-display').value = currentExpression;
}

function clearDisplay() {
    currentExpression = '';
    document.getElementById('calc-display').value = '';
}

function backspace() {
    currentExpression = currentExpression.slice(0, -1);
    document.getElementById('calc-display').value = currentExpression;
}

async function calculate() {
    if (!currentExpression) return;

    try {
        const response = await fetch('/api/calculate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                expression: currentExpression
            })
        });

        const data = await response.json();

        if (data.success) {
            document.getElementById('calc-display').value = data.result;
            addToHistory(`${currentExpression} = ${data.result}`);
            currentExpression = data.result;
        } else {
            showAlert(data.error, 'error');
            currentExpression = '';
            document.getElementById('calc-display').value = '';
        }
    } catch (error) {
        showAlert('Erro ao calcular: ' + error.message, 'error');
    }
}

function addToHistory(text) {
    const historyDiv = document.getElementById('history');
    const item = document.createElement('div');
    item.className = 'history-item';
    item.textContent = text;
    historyDiv.insertBefore(item, historyDiv.firstChild);
}

async function clearHistory() {
    try {
        await fetch('/api/history', {
            method: 'DELETE'
        });
        document.getElementById('history').innerHTML = '';
    } catch (error) {
        console.error('Erro ao limpar histórico:', error);
    }
}

// Integration Functions
async function calculateIntegral() {
    const functionInput = document.getElementById('function-input').value;
    const lowerBound = parseFloat(document.getElementById('lower-bound').value);
    const upperBound = parseFloat(document.getElementById('upper-bound').value);
    const method = document.getElementById('method-select').value;
    const intervals = parseInt(document.getElementById('intervals-input').value);

    if (!functionInput) {
        showAlert('Por favor, insira uma função', 'error');
        return;
    }

    if (isNaN(lowerBound) || isNaN(upperBound)) {
        showAlert('Por favor, insira limites válidos', 'error');
        return;
    }

    if (lowerBound >= upperBound) {
        showAlert('O limite inferior deve ser menor que o superior', 'error');
        return;
    }

    // Show loading
    const resultSection = document.getElementById('result-section');
    resultSection.style.display = 'block';
    resultSection.innerHTML = '<div class="spinner"></div>';

    try {
        const response = await fetch('/api/integrate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                function: functionInput,
                lower_bound: lowerBound,
                upper_bound: upperBound,
                method: method,
                intervals: intervals
            })
        });

        const data = await response.json();

        if (data.success) {
            displayResult(data, functionInput, lowerBound, upperBound, method);
            if (data.plot_data) {
                plotGraph(data.plot_data, functionInput);
            }
        } else {
            resultSection.innerHTML = `<div class="alert alert-error">${data.error_message}</div>`;
        }
    } catch (error) {
        resultSection.innerHTML = `<div class="alert alert-error">Erro ao calcular integral: ${error.message}</div>`;
    }
}

function displayResult(data, func, a, b, method) {
    const resultSection = document.getElementById('result-section');

    let html = `
        <h2>Resultado da Integração</h2>
        <div class="result-content">
            <div class="result-item">
                <strong>Função:</strong> f(x) = ${func}
            </div>
            <div class="result-item">
                <strong>Intervalo:</strong> [${a}, ${b}]
            </div>
            <div class="result-item">
                <strong>Método:</strong> ${method}
            </div>
            <div class="result-item">
                <strong>Resultado:</strong> <span class="result-value">${data.result.toFixed(10)}</span>
            </div>
    `;

    if (data.error_estimate !== null && data.error_estimate !== undefined) {
        html += `
            <div class="result-item">
                <strong>Erro Estimado:</strong> ${data.error_estimate.toExponential(2)}
            </div>
        `;
    }

    html += '</div>';
    resultSection.innerHTML = html;
}

async function plotFunction() {
    const functionInput = document.getElementById('function-input').value;
    const lowerBound = parseFloat(document.getElementById('lower-bound').value);
    const upperBound = parseFloat(document.getElementById('upper-bound').value);

    if (!functionInput) {
        showAlert('Por favor, insira uma função', 'error');
        return;
    }

    if (isNaN(lowerBound) || isNaN(upperBound)) {
        showAlert('Por favor, insira limites válidos', 'error');
        return;
    }

    try {
        // Use the integration endpoint to get plot data
        const response = await fetch('/api/integrate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                function: functionInput,
                lower_bound: lowerBound,
                upper_bound: upperBound,
                method: 'Simpson',
                intervals: 1000
            })
        });

        const data = await response.json();

        if (data.success && data.plot_data) {
            plotGraph(data.plot_data, functionInput);
        } else {
            showAlert(data.error_message || 'Erro ao plotar função', 'error');
        }
    } catch (error) {
        showAlert('Erro ao plotar função: ' + error.message, 'error');
    }
}

function plotGraph(plotData, functionStr) {
    const trace1 = {
        x: plotData.x,
        y: plotData.y,
        type: 'scatter',
        mode: 'lines',
        name: `f(x) = ${functionStr}`,
        line: {
            color: '#2563eb',
            width: 3
        }
    };

    const trace2 = {
        x: plotData.x_fill,
        y: plotData.y_fill,
        fill: 'tozeroy',
        type: 'scatter',
        mode: 'none',
        name: 'Área Integrada',
        fillcolor: 'rgba(16, 185, 129, 0.3)'
    };

    const layout = {
        title: {
            text: `Gráfico de f(x) = ${functionStr}`,
            font: {
                size: 20,
                family: 'Arial, sans-serif'
            }
        },
        xaxis: {
            title: 'x',
            gridcolor: '#e2e8f0',
            showgrid: true,
            zeroline: true,
            zerolinecolor: '#000',
            zerolinewidth: 2
        },
        yaxis: {
            title: 'f(x)',
            gridcolor: '#e2e8f0',
            showgrid: true,
            zeroline: true,
            zerolinecolor: '#000',
            zerolinewidth: 2
        },
        shapes: [
            {
                type: 'line',
                x0: plotData.lower_bound,
                y0: Math.min(...plotData.y) - 1,
                x1: plotData.lower_bound,
                y1: Math.max(...plotData.y) + 1,
                line: {
                    color: '#ef4444',
                    width: 2,
                    dash: 'dash'
                }
            },
            {
                type: 'line',
                x0: plotData.upper_bound,
                y0: Math.min(...plotData.y) - 1,
                x1: plotData.upper_bound,
                y1: Math.max(...plotData.y) + 1,
                line: {
                    color: '#ef4444',
                    width: 2,
                    dash: 'dash'
                }
            }
        ],
        annotations: [
            {
                x: plotData.lower_bound,
                y: Math.max(...plotData.y),
                text: `a = ${plotData.lower_bound}`,
                showarrow: true,
                arrowhead: 2,
                ax: -40,
                ay: -40
            },
            {
                x: plotData.upper_bound,
                y: Math.max(...plotData.y),
                text: `b = ${plotData.upper_bound}`,
                showarrow: true,
                arrowhead: 2,
                ax: 40,
                ay: -40
            }
        ],
        showlegend: true,
        legend: {
            x: 0.02,
            y: 0.98,
            bgcolor: 'rgba(255, 255, 255, 0.8)',
            bordercolor: '#e2e8f0',
            borderwidth: 1
        },
        hovermode: 'closest',
        plot_bgcolor: '#f8fafc',
        paper_bgcolor: '#ffffff'
    };

    const config = {
        responsive: true,
        displayModeBar: true,
        displaylogo: false,
        modeBarButtonsToRemove: ['select2d', 'lasso2d']
    };

    Plotly.newPlot('plot-container', [trace2, trace1], layout, config);
}

// Utility Functions
function showAlert(message, type = 'info') {
    // Create alert element
    const alert = document.createElement('div');
    alert.className = `alert alert-${type}`;
    alert.textContent = message;

    // Insert at the top of the active tab
    const activeTab = document.querySelector('.tab-content.active');
    activeTab.insertBefore(alert, activeTab.firstChild);

    // Remove after 5 seconds
    setTimeout(() => {
        alert.remove();
    }, 5000);
}

// Keyboard support for calculator
document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('calc-display').addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            calculate();
        }
    });

    // Allow direct typing in calculator display
    document.getElementById('calc-display').addEventListener('input', function(e) {
        currentExpression = e.target.value;
    });

    // Keyboard support for integration
    document.getElementById('function-input').addEventListener('keypress', function(e) {
        if (e.key === 'Enter' && e.ctrlKey) {
            calculateIntegral();
        }
    });
});

// Load calculation history on page load
window.addEventListener('load', async function() {
    try {
        const response = await fetch('/api/history');
        const data = await response.json();
        if (data.history && data.history.length > 0) {
            data.history.forEach(item => addToHistory(item));
        }
    } catch (error) {
        console.error('Erro ao carregar histórico:', error);
    }
});
