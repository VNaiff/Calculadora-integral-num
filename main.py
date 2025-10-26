#!/usr/bin/env python3
"""
Calculadora com Integração Numérica
Main entry point for the application.
"""

import sys
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from src.gui.main_window import CalculatorApp


def main():
    """Main function to run the calculator application."""
    # Create root window with modern theme
    root = ttk.Window(themename="cosmo")  # Modern blue theme

    # Create and run app
    app = CalculatorApp(root)
    app.run()


if __name__ == "__main__":
    main()
