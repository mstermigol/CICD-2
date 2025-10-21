"""
Módulo principal de la aplicación Flask de la calculadora.

Define la aplicación web, gestiona las rutas y procesa las
operaciones aritméticas básicas (suma, resta, multiplicación,
división, potencia y raíz cuadrada) mediante un formulario HTML.
"""

import os
from flask import Flask, render_template, request
from .calculadora import (
    sumar,
    restar,
    multiplicar,
    dividir,
    potencia,
    raiz_cuadrada,
)

app = Flask(__name__)


def realizar_operacion(operacion, num1_str, num2_str=None):
    """
    Ejecuta la operación aritmética seleccionada.
    Separa la lógica para reducir la complejidad de la vista principal.
    """
    if operacion in ("raiz", "raiz_cuadrada"):
        num1 = float(num1_str)
        return raiz_cuadrada(num1)

    num1 = float(num1_str)
    num2 = float(num2_str)

    operaciones = {
        "sumar": sumar,
        "restar": restar,
        "multiplicar": multiplicar,
        "dividir": dividir,
        "potencia": potencia,
    }

    if operacion not in operaciones:
        return "Operación no válida"

    return operaciones[operacion](num1, num2)


def extraer_form(req):
    """Obtiene y normaliza los campos del formulario."""
    return (
        (req.form.get("operacion") or "").strip(),
        (req.form.get("num1") or "").strip(),
        (req.form.get("num2") or "").strip(),
    )


def mensaje_error_value_error(operacion, ve):
    """Mapea ValueError a un mensaje de error de usuario."""
    msg = (str(ve) or "").strip()
    if operacion in ("raiz", "raiz_cuadrada") and msg:
        return f"Error: {msg}"
    return "Error: Introduce números válidos"


@app.route("/", methods=["GET", "POST"])
def index():
    """
    Maneja la ruta principal de la aplicación.

    - GET: muestra el formulario.
    - POST: procesa los datos, realiza la operación y muestra el resultado.
    """
    if request.method != "POST":
        return render_template("index.html", resultado=None)

    operacion, num1_str, num2_str = extraer_form(request)

    try:
        resultado = realizar_operacion(operacion, num1_str, num2_str)
    except ValueError as ve:
        resultado = mensaje_error_value_error(operacion, ve)
    except ZeroDivisionError:
        resultado = "Error: No se puede dividir por cero"

    return render_template("index.html", resultado=resultado)


@app.route("/health")
def health():
    """Endpoint de verificación de salud para el ALB."""
    return "OK", 200


if __name__ == "__main__":  # pragma: no cover
    app_port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=app_port, debug=False)
