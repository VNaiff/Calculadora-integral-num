"""
Numerical integration methods.
Implements various numerical integration techniques in a modular way.
"""

import numpy as np
from enum import Enum
from typing import Callable, Tuple, Optional
import math


class IntegrationMethod(Enum):
    """Available integration methods."""
    TRAPEZOIDAL = "Trapezoidal"
    SIMPSON = "Simpson"
    SIMPSON_3_8 = "Simpson 3/8"
    ROMBERG = "Romberg"
    MONTE_CARLO = "Monte Carlo"


class NumericalIntegrator:
    """
    Numerical integration calculator.
    Implements multiple methods for numerical integration.
    """

    def __init__(self):
        """Initialize the integrator."""
        self.last_result = None
        self.last_error_estimate = None

    def integrate(
        self,
        func: Callable[[float], float],
        a: float,
        b: float,
        method: IntegrationMethod = IntegrationMethod.SIMPSON,
        n: int = 1000,
        **kwargs
    ) -> Tuple[float, Optional[float]]:
        """
        Integrate a function using the specified method.

        Args:
            func: Function to integrate
            a: Lower bound
            b: Upper bound
            method: Integration method to use
            n: Number of intervals/subdivisions
            **kwargs: Additional method-specific parameters

        Returns:
            Tuple of (integral value, error estimate)
        """
        if a >= b:
            raise ValueError("Lower bound must be less than upper bound")

        if method == IntegrationMethod.TRAPEZOIDAL:
            result = self._trapezoidal(func, a, b, n)
            error = None
        elif method == IntegrationMethod.SIMPSON:
            result = self._simpson(func, a, b, n)
            error = None
        elif method == IntegrationMethod.SIMPSON_3_8:
            result = self._simpson_3_8(func, a, b, n)
            error = None
        elif method == IntegrationMethod.ROMBERG:
            result, error = self._romberg(func, a, b, kwargs.get('max_iter', 10))
        elif method == IntegrationMethod.MONTE_CARLO:
            result, error = self._monte_carlo(func, a, b, kwargs.get('samples', 10000))
        else:
            raise ValueError(f"Unknown integration method: {method}")

        self.last_result = result
        self.last_error_estimate = error

        return result, error

    def _trapezoidal(self, func: Callable, a: float, b: float, n: int) -> float:
        """
        Trapezoidal rule for numerical integration.

        Args:
            func: Function to integrate
            a: Lower bound
            b: Upper bound
            n: Number of intervals

        Returns:
            Integral approximation
        """
        h = (b - a) / n
        x = np.linspace(a, b, n + 1)
        y = np.array([func(xi) for xi in x])

        # Trapezoidal rule: h/2 * (y0 + 2*y1 + 2*y2 + ... + 2*yn-1 + yn)
        result = h * (0.5 * y[0] + np.sum(y[1:-1]) + 0.5 * y[-1])

        return result

    def _simpson(self, func: Callable, a: float, b: float, n: int) -> float:
        """
        Simpson's 1/3 rule for numerical integration.

        Args:
            func: Function to integrate
            a: Lower bound
            b: Upper bound
            n: Number of intervals (must be even)

        Returns:
            Integral approximation
        """
        # Ensure n is even
        if n % 2 != 0:
            n += 1

        h = (b - a) / n
        x = np.linspace(a, b, n + 1)
        y = np.array([func(xi) for xi in x])

        # Simpson's rule: h/3 * (y0 + 4*y1 + 2*y2 + 4*y3 + ... + yn)
        result = h / 3 * (
            y[0] +
            4 * np.sum(y[1:-1:2]) +
            2 * np.sum(y[2:-1:2]) +
            y[-1]
        )

        return result

    def _simpson_3_8(self, func: Callable, a: float, b: float, n: int) -> float:
        """
        Simpson's 3/8 rule for numerical integration.

        Args:
            func: Function to integrate
            a: Lower bound
            b: Upper bound
            n: Number of intervals (must be divisible by 3)

        Returns:
            Integral approximation
        """
        # Ensure n is divisible by 3
        while n % 3 != 0:
            n += 1

        h = (b - a) / n
        x = np.linspace(a, b, n + 1)
        y = np.array([func(xi) for xi in x])

        # Simpson's 3/8 rule
        result = 3 * h / 8 * (
            y[0] +
            3 * np.sum(y[1:-1:3]) +
            3 * np.sum(y[2:-1:3]) +
            2 * np.sum(y[3:-1:3]) +
            y[-1]
        )

        return result

    def _romberg(
        self,
        func: Callable,
        a: float,
        b: float,
        max_iter: int = 10,
        tol: float = 1e-8
    ) -> Tuple[float, float]:
        """
        Romberg integration method.

        Args:
            func: Function to integrate
            a: Lower bound
            b: Upper bound
            max_iter: Maximum number of iterations
            tol: Tolerance for convergence

        Returns:
            Tuple of (integral value, error estimate)
        """
        R = np.zeros((max_iter, max_iter))

        # First approximation using trapezoidal rule
        R[0, 0] = 0.5 * (b - a) * (func(a) + func(b))

        for i in range(1, max_iter):
            # Trapezoidal approximation with 2^i intervals
            h = (b - a) / (2 ** i)
            sum_term = 0
            for k in range(1, 2 ** (i - 1) + 1):
                sum_term += func(a + (2 * k - 1) * h)
            R[i, 0] = 0.5 * R[i - 1, 0] + h * sum_term

            # Richardson extrapolation
            for j in range(1, i + 1):
                R[i, j] = R[i, j - 1] + (R[i, j - 1] - R[i - 1, j - 1]) / (4 ** j - 1)

            # Check for convergence
            if i > 0:
                error = abs(R[i, i] - R[i - 1, i - 1])
                if error < tol:
                    return R[i, i], error

        return R[max_iter - 1, max_iter - 1], abs(R[max_iter - 1, max_iter - 1] - R[max_iter - 2, max_iter - 2])

    def _monte_carlo(
        self,
        func: Callable,
        a: float,
        b: float,
        samples: int = 10000
    ) -> Tuple[float, float]:
        """
        Monte Carlo integration method.

        Args:
            func: Function to integrate
            a: Lower bound
            b: Upper bound
            samples: Number of random samples

        Returns:
            Tuple of (integral value, error estimate)
        """
        # Generate random points
        x_random = np.random.uniform(a, b, samples)
        y_values = np.array([func(x) for x in x_random])

        # Calculate integral
        integral = (b - a) * np.mean(y_values)

        # Estimate error using standard deviation
        error = (b - a) * np.std(y_values) / np.sqrt(samples)

        return integral, error

    @staticmethod
    def parse_function(expression: str) -> Callable[[float], float]:
        """
        Parse a string expression into a callable function.

        Args:
            expression: String representation of the function (e.g., "x**2 + 2*x + 1")

        Returns:
            Callable function

        Example:
            >>> func = NumericalIntegrator.parse_function("x**2")
            >>> func(3)
            9.0
        """
        # Safe namespace for evaluation
        safe_dict = {
            '__builtins__': {},
            'abs': abs,
            'sqrt': np.sqrt,
            'sin': np.sin,
            'cos': np.cos,
            'tan': np.tan,
            'asin': np.arcsin,
            'acos': np.arccos,
            'atan': np.arctan,
            'log': np.log,
            'ln': np.log,
            'log10': np.log10,
            'exp': np.exp,
            'pi': np.pi,
            'e': np.e,
            'sinh': np.sinh,
            'cosh': np.cosh,
            'tanh': np.tanh,
        }

        # Preprocess expression
        expression = expression.replace('^', '**')
        expression = expression.replace('√', 'sqrt')

        def func(x):
            local_dict = safe_dict.copy()
            local_dict['x'] = x
            try:
                return eval(expression, local_dict)
            except Exception as e:
                raise ValueError(f"Error evaluating function at x={x}: {str(e)}")

        return func
