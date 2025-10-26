"""
Main calculator window with modern GUI.
Uses ttkbootstrap for a modern, professional appearance.
"""

import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox, scrolledtext
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

from src.core.calculator import Calculator
from src.integrators.numerical_integrator import NumericalIntegrator, IntegrationMethod


class CalculatorApp:
    """Main calculator application with GUI."""

    def __init__(self, root):
        """Initialize the calculator application."""
        self.root = root
        self.root.title("Calculadora com Integração Numérica")
        self.root.geometry("900x700")

        # Core components
        self.calculator = Calculator()
        self.integrator = NumericalIntegrator()

        # Current expression
        self.current_expression = ""

        # Create GUI
        self._create_widgets()

    def _create_widgets(self):
        """Create all GUI widgets."""
        # Create notebook for tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=BOTH, expand=YES, padx=5, pady=5)

        # Create tabs
        self.calc_frame = ttk.Frame(self.notebook)
        self.integral_frame = ttk.Frame(self.notebook)

        self.notebook.add(self.calc_frame, text="Calculadora")
        self.notebook.add(self.integral_frame, text="Integração Numérica")

        # Build calculator tab
        self._build_calculator_tab()

        # Build integral tab
        self._build_integral_tab()

    def _build_calculator_tab(self):
        """Build the calculator tab."""
        # Display frame
        display_frame = ttk.Frame(self.calc_frame)
        display_frame.pack(fill=X, padx=10, pady=10)

        # Display
        self.display = ttk.Entry(
            display_frame,
            font=('Arial', 24),
            justify=RIGHT
        )
        self.display.pack(fill=X, ipady=10)

        # Buttons frame
        buttons_frame = ttk.Frame(self.calc_frame)
        buttons_frame.pack(fill=BOTH, expand=YES, padx=10, pady=5)

        # Button layout
        buttons = [
            ['7', '8', '9', '/', 'C'],
            ['4', '5', '6', '*', '('],
            ['1', '2', '3', '-', ')'],
            ['0', '.', '=', '+', '←'],
            ['sin', 'cos', 'tan', 'sqrt', '^'],
            ['π', 'e', 'log', 'ln', 'exp'],
        ]

        for i, row in enumerate(buttons):
            for j, btn_text in enumerate(row):
                btn = ttk.Button(
                    buttons_frame,
                    text=btn_text,
                    command=lambda t=btn_text: self._on_button_click(t),
                    bootstyle=self._get_button_style(btn_text)
                )
                btn.grid(row=i, column=j, sticky='nsew', padx=2, pady=2)

        # Configure grid weights
        for i in range(len(buttons)):
            buttons_frame.grid_rowconfigure(i, weight=1)
        for j in range(len(buttons[0])):
            buttons_frame.grid_columnconfigure(j, weight=1)

        # History frame
        history_frame = ttk.LabelFrame(self.calc_frame, text="Histórico", padding=10)
        history_frame.pack(fill=BOTH, expand=YES, padx=10, pady=5)

        self.history_text = scrolledtext.ScrolledText(
            history_frame,
            height=8,
            font=('Arial', 10),
            state='disabled'
        )
        self.history_text.pack(fill=BOTH, expand=YES)

    def _build_integral_tab(self):
        """Build the numerical integration tab."""
        # Input frame
        input_frame = ttk.LabelFrame(self.integral_frame, text="Entrada", padding=10)
        input_frame.pack(fill=X, padx=10, pady=10)

        # Function input
        ttk.Label(input_frame, text="Função f(x):").grid(row=0, column=0, sticky=W, pady=5)
        self.func_entry = ttk.Entry(input_frame, font=('Arial', 12))
        self.func_entry.grid(row=0, column=1, sticky=EW, padx=5, pady=5)
        self.func_entry.insert(0, "x**2")

        # Lower bound
        ttk.Label(input_frame, text="Limite inferior (a):").grid(row=1, column=0, sticky=W, pady=5)
        self.lower_bound = ttk.Entry(input_frame, font=('Arial', 12))
        self.lower_bound.grid(row=1, column=1, sticky=EW, padx=5, pady=5)
        self.lower_bound.insert(0, "0")

        # Upper bound
        ttk.Label(input_frame, text="Limite superior (b):").grid(row=2, column=0, sticky=W, pady=5)
        self.upper_bound = ttk.Entry(input_frame, font=('Arial', 12))
        self.upper_bound.grid(row=2, column=1, sticky=EW, padx=5, pady=5)
        self.upper_bound.insert(0, "1")

        # Number of intervals
        ttk.Label(input_frame, text="Número de intervalos:").grid(row=3, column=0, sticky=W, pady=5)
        self.intervals = ttk.Entry(input_frame, font=('Arial', 12))
        self.intervals.grid(row=3, column=1, sticky=EW, padx=5, pady=5)
        self.intervals.insert(0, "1000")

        # Method selection
        ttk.Label(input_frame, text="Método:").grid(row=4, column=0, sticky=W, pady=5)
        self.method_var = ttk.StringVar(value="Simpson")
        methods = [method.value for method in IntegrationMethod]
        self.method_combo = ttk.Combobox(
            input_frame,
            textvariable=self.method_var,
            values=methods,
            state='readonly',
            font=('Arial', 12)
        )
        self.method_combo.grid(row=4, column=1, sticky=EW, padx=5, pady=5)

        input_frame.grid_columnconfigure(1, weight=1)

        # Calculate button
        calc_btn = ttk.Button(
            input_frame,
            text="Calcular Integral",
            command=self._calculate_integral,
            bootstyle="success"
        )
        calc_btn.grid(row=5, column=0, columnspan=2, pady=10, sticky=EW)

        # Plot button
        plot_btn = ttk.Button(
            input_frame,
            text="Plotar Função",
            command=self._plot_function,
            bootstyle="info"
        )
        plot_btn.grid(row=6, column=0, columnspan=2, pady=5, sticky=EW)

        # Result frame
        result_frame = ttk.LabelFrame(self.integral_frame, text="Resultado", padding=10)
        result_frame.pack(fill=X, padx=10, pady=5)

        self.result_text = scrolledtext.ScrolledText(
            result_frame,
            height=8,
            font=('Arial', 11),
            state='disabled'
        )
        self.result_text.pack(fill=BOTH, expand=YES)

    def _get_button_style(self, btn_text):
        """Get button style based on button text."""
        if btn_text == '=':
            return 'success'
        elif btn_text in ['C', '←']:
            return 'danger'
        elif btn_text in ['+', '-', '*', '/', '^']:
            return 'warning'
        else:
            return 'primary'

    def _on_button_click(self, btn_text):
        """Handle button click events."""
        if btn_text == '=':
            self._calculate()
        elif btn_text == 'C':
            self._clear()
        elif btn_text == '←':
            self._backspace()
        elif btn_text == 'π':
            self.current_expression += 'pi'
            self.display.delete(0, END)
            self.display.insert(0, self.current_expression)
        elif btn_text == 'e':
            self.current_expression += 'e'
            self.display.delete(0, END)
            self.display.insert(0, self.current_expression)
        elif btn_text in ['sin', 'cos', 'tan', 'sqrt', 'log', 'ln', 'exp']:
            self.current_expression += btn_text + '('
            self.display.delete(0, END)
            self.display.insert(0, self.current_expression)
        elif btn_text == '^':
            self.current_expression += '**'
            self.display.delete(0, END)
            self.display.insert(0, self.current_expression)
        else:
            self.current_expression += btn_text
            self.display.delete(0, END)
            self.display.insert(0, self.current_expression)

    def _calculate(self):
        """Calculate the current expression."""
        if not self.current_expression:
            return

        result = self.calculator.evaluate(self.current_expression)

        if isinstance(result, str):  # Error occurred
            messagebox.showerror("Erro", result)
        else:
            self.display.delete(0, END)
            self.display.insert(0, str(result))
            self._add_to_history(f"{self.current_expression} = {result}")
            self.current_expression = str(result)

    def _clear(self):
        """Clear the display."""
        self.current_expression = ""
        self.display.delete(0, END)

    def _backspace(self):
        """Delete last character."""
        self.current_expression = self.current_expression[:-1]
        self.display.delete(0, END)
        self.display.insert(0, self.current_expression)

    def _add_to_history(self, text):
        """Add text to history."""
        self.history_text.config(state='normal')
        self.history_text.insert(END, text + '\n')
        self.history_text.see(END)
        self.history_text.config(state='disabled')

    def _calculate_integral(self):
        """Calculate the numerical integral."""
        try:
            # Get inputs
            func_str = self.func_entry.get()
            a = float(self.lower_bound.get())
            b = float(self.upper_bound.get())
            n = int(self.intervals.get())
            method_name = self.method_var.get()

            # Parse function
            func = NumericalIntegrator.parse_function(func_str)

            # Get method enum
            method = None
            for m in IntegrationMethod:
                if m.value == method_name:
                    method = m
                    break

            # Calculate integral
            if method in [IntegrationMethod.ROMBERG]:
                result, error = self.integrator.integrate(func, a, b, method=method)
            elif method == IntegrationMethod.MONTE_CARLO:
                result, error = self.integrator.integrate(func, a, b, method=method, samples=n)
            else:
                result, error = self.integrator.integrate(func, a, b, method=method, n=n)

            # Display result
            self.result_text.config(state='normal')
            self.result_text.delete(1.0, END)
            self.result_text.insert(END, f"Função: f(x) = {func_str}\n")
            self.result_text.insert(END, f"Intervalo: [{a}, {b}]\n")
            self.result_text.insert(END, f"Método: {method_name}\n")
            self.result_text.insert(END, f"\nResultado: {result:.10f}\n")
            if error is not None:
                self.result_text.insert(END, f"Erro estimado: {error:.2e}\n")
            self.result_text.config(state='disabled')

        except ValueError as e:
            messagebox.showerror("Erro", f"Erro nos valores de entrada:\n{str(e)}")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao calcular integral:\n{str(e)}")

    def _plot_function(self):
        """Plot the function and shaded integral area."""
        try:
            # Get inputs
            func_str = self.func_entry.get()
            a = float(self.lower_bound.get())
            b = float(self.upper_bound.get())

            # Parse function
            func = NumericalIntegrator.parse_function(func_str)

            # Create plot window
            plot_window = ttk.Toplevel(self.root)
            plot_window.title("Gráfico da Função")
            plot_window.geometry("800x600")

            # Create figure
            fig, ax = plt.subplots(figsize=(8, 6))

            # Plot function
            x = np.linspace(a - 1, b + 1, 1000)
            y = [func(xi) for xi in x]
            ax.plot(x, y, 'b-', linewidth=2, label=f'f(x) = {func_str}')

            # Shade integral area
            x_fill = np.linspace(a, b, 1000)
            y_fill = [func(xi) for xi in x_fill]
            ax.fill_between(x_fill, 0, y_fill, alpha=0.3, color='green', label='Área integrada')

            # Mark bounds
            ax.axvline(x=a, color='r', linestyle='--', label=f'a = {a}')
            ax.axvline(x=b, color='r', linestyle='--', label=f'b = {b}')
            ax.axhline(y=0, color='k', linestyle='-', linewidth=0.5)

            ax.set_xlabel('x', fontsize=12)
            ax.set_ylabel('f(x)', fontsize=12)
            ax.set_title(f'Gráfico de f(x) = {func_str}', fontsize=14)
            ax.legend()
            ax.grid(True, alpha=0.3)

            # Embed in tkinter
            canvas = FigureCanvasTkAgg(fig, master=plot_window)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=BOTH, expand=YES)

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao plotar função:\n{str(e)}")

    def run(self):
        """Run the application."""
        self.root.mainloop()
