#!/usr/bin/env python3
"""
Script to run the web application.
"""

import uvicorn
import sys
import os

# Add the project root to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def main():
    """Run the web application."""
    print("=" * 60)
    print("Calculadora com Integração Numérica - Web App")
    print("=" * 60)
    print("\nIniciando servidor...")
    print("\nAcesse a aplicação em: http://localhost:8000")
    print("Pressione CTRL+C para parar o servidor\n")
    print("=" * 60)

    uvicorn.run(
        "webapp.app:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )


if __name__ == "__main__":
    main()
