"""
Módulo principal de la aplicación Flask de la calculadora.

Este archivo define la aplicación web, gestiona las rutas y
procesa las operaciones aritméticas básicas (suma, resta,
multiplicación y división) a través del formulario HTML.
"""

import os
from flask import Flask, render_template, request
from .calculadora import sumar, restar, multiplicar, dividir, potencia, raiz_cuadrada

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    """
    Maneja la ruta principal de la aplicación.

    - Si el método es GET: muestra el formulario de la calculadora.
    - Si el método es POST: procesa los datos enviados, realiza la operación
      seleccionada y devuelve el resultado.
    """
    resultado = None

    if request.method == "POST":
        operacion = (request.form.get("operacion") or "").strip()
        num1_str = (request.form.get("num1") or "").strip()
        num2_str = (request.form.get("num2") or "").strip()

        try:
            if operacion in ("raiz", "raiz_cuadrada"):
                num1 = float(num1_str)
                resultado = raiz_cuadrada(num1)
            else:
                num1 = float(num1_str)
                num2 = float(num2_str)

                if operacion == "sumar":
                    resultado = sumar(num1, num2)
                elif operacion == "restar":
                    resultado = restar(num1, num2)
                elif operacion == "multiplicar":
                    resultado = multiplicar(num1, num2)
                elif operacion == "dividir":
                    resultado = dividir(num1, num2)
                elif operacion == "potencia":
                    resultado = potencia(num1, num2)
                else:
                    resultado = "Operación no válida"

        except ValueError as ve:
            msg = str(ve) or "Introduce números válidos"
            resultado = f"Error: {msg}"
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
