"""
Core calculator operations.
Provides basic arithmetic and advanced mathematical operations.
"""

import math
import re
from typing import Union, Optional


class Calculator:
    """
    Core calculator class with basic and advanced operations.
    Designed to be modular and extensible.
    """

    def __init__(self):
        """Initialize the calculator."""
        self.history = []
        self.memory = 0

    def evaluate(self, expression: str) -> Union[float, str]:
        """
        Evaluate a mathematical expression.

        Args:
            expression: String containing the mathematical expression

        Returns:
            Result of the evaluation or error message
        """
        try:
            # Clean the expression
            expression = expression.strip()

            # Replace common mathematical notation
            expression = self._preprocess_expression(expression)

            # Safe evaluation using eval with restricted namespace
            safe_dict = {
                '__builtins__': {},
                'abs': abs,
                'round': round,
                'pow': pow,
                'sqrt': math.sqrt,
                'sin': math.sin,
                'cos': math.cos,
                'tan': math.tan,
                'asin': math.asin,
                'acos': math.acos,
                'atan': math.atan,
                'log': math.log,
                'log10': math.log10,
                'exp': math.exp,
                'pi': math.pi,
                'e': math.e,
            }

            result = eval(expression, safe_dict)

            # Add to history
            self.history.append(f"{expression} = {result}")

            return result

        except ZeroDivisionError:
            return "Erro: Divisão por zero"
        except Exception as e:
            return f"Erro: {str(e)}"

    def _preprocess_expression(self, expr: str) -> str:
        """
        Preprocess expression to handle common mathematical notation.

        Args:
            expr: Raw expression string

        Returns:
            Processed expression string
        """
        # Replace × with *
        expr = expr.replace('×', '*')
        # Replace ÷ with /
        expr = expr.replace('÷', '/')
        # Replace ^ with **
        expr = expr.replace('^', '**')

        return expr

    # Memory operations
    def memory_store(self, value: float):
        """Store value in memory."""
        self.memory = value

    def memory_recall(self) -> float:
        """Recall value from memory."""
        return self.memory

    def memory_clear(self):
        """Clear memory."""
        self.memory = 0

    def memory_add(self, value: float):
        """Add value to memory."""
        self.memory += value

    def memory_subtract(self, value: float):
        """Subtract value from memory."""
        self.memory -= value

    def clear_history(self):
        """Clear calculation history."""
        self.history.clear()

    def get_history(self) -> list:
        """Get calculation history."""
        return self.history.copy()
