"""
FastAPI Web Application for Numerical Integral Calculator
"""

from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List, Optional
import numpy as np
import io
import base64
import matplotlib
matplotlib.use('Agg')  # Use non-GUI backend
import matplotlib.pyplot as plt

from src.core.calculator import Calculator
from src.integrators.numerical_integrator import NumericalIntegrator, IntegrationMethod

# Initialize FastAPI app
app = FastAPI(
    title="Calculadora com Integração Numérica",
    description="Web app para cálculos e integração numérica",
    version="1.0.0"
)

# Mount static files and templates
app.mount("/static", StaticFiles(directory="webapp/static"), name="static")
templates = Jinja2Templates(directory="webapp/templates")

# Initialize calculator and integrator
calculator = Calculator()
integrator = NumericalIntegrator()


# Pydantic models for request/response
class CalculationRequest(BaseModel):
    expression: str


class CalculationResponse(BaseModel):
    result: str
    success: bool
    error: Optional[str] = None


class IntegrationRequest(BaseModel):
    function: str
    lower_bound: float
    upper_bound: float
    method: str
    intervals: int = 1000


class IntegrationResponse(BaseModel):
    result: float
    error_estimate: Optional[float] = None
    success: bool
    error_message: Optional[str] = None
    plot_data: Optional[dict] = None


# Routes
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Render the main page."""
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/api/calculate", response_model=CalculationResponse)
async def calculate(req: CalculationRequest):
    """
    Calculate a mathematical expression.

    Args:
        req: Calculation request with expression

    Returns:
        Calculation result or error
    """
    try:
        result = calculator.evaluate(req.expression)

        if isinstance(result, str) and result.startswith("Erro"):
            return CalculationResponse(
                result="",
                success=False,
                error=result
            )

        return CalculationResponse(
            result=str(result),
            success=True
        )
    except Exception as e:
        return CalculationResponse(
            result="",
            success=False,
            error=f"Erro: {str(e)}"
        )


@app.post("/api/integrate", response_model=IntegrationResponse)
async def integrate(req: IntegrationRequest):
    """
    Calculate numerical integration.

    Args:
        req: Integration request with function, bounds, and method

    Returns:
        Integration result with optional error estimate and plot data
    """
    try:
        # Parse function
        func = NumericalIntegrator.parse_function(req.function)

        # Get method enum
        method = None
        for m in IntegrationMethod:
            if m.value == req.method:
                method = m
                break

        if method is None:
            raise ValueError(f"Método desconhecido: {req.method}")

        # Calculate integration
        if method == IntegrationMethod.ROMBERG:
            result, error = integrator.integrate(
                func,
                req.lower_bound,
                req.upper_bound,
                method=method
            )
        elif method == IntegrationMethod.MONTE_CARLO:
            result, error = integrator.integrate(
                func,
                req.lower_bound,
                req.upper_bound,
                method=method,
                samples=req.intervals
            )
        else:
            result, error = integrator.integrate(
                func,
                req.lower_bound,
                req.upper_bound,
                method=method,
                n=req.intervals
            )

        # Generate plot data
        x_values = np.linspace(req.lower_bound - 1, req.upper_bound + 1, 500)
        y_values = [func(x) for x in x_values]

        x_fill = np.linspace(req.lower_bound, req.upper_bound, 500)
        y_fill = [func(x) for x in x_fill]

        plot_data = {
            "x": x_values.tolist(),
            "y": y_values,
            "x_fill": x_fill.tolist(),
            "y_fill": y_fill,
            "lower_bound": req.lower_bound,
            "upper_bound": req.upper_bound
        }

        return IntegrationResponse(
            result=result,
            error_estimate=error,
            success=True,
            plot_data=plot_data
        )

    except Exception as e:
        return IntegrationResponse(
            result=0.0,
            success=False,
            error_message=f"Erro: {str(e)}"
        )


@app.get("/api/methods")
async def get_methods():
    """Get available integration methods."""
    methods = [{"name": method.value, "value": method.value} for method in IntegrationMethod]
    return {"methods": methods}


@app.get("/api/history")
async def get_history():
    """Get calculation history."""
    return {"history": calculator.get_history()}


@app.delete("/api/history")
async def clear_history():
    """Clear calculation history."""
    calculator.clear_history()
    return {"message": "Histórico limpo com sucesso"}


# Health check
@app.get("/health")
async def health():
    """Health check endpoint."""
    return {"status": "healthy", "version": "1.0.0"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
