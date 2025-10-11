"""
Módulo principal de la aplicación Flask de la calculadora.

Este archivo define la aplicación web, gestiona las rutas y
procesa las operaciones aritméticas básicas (suma, resta,
multiplicación y división) a través del formulario HTML.
"""

from flask import Flask, render_template, request
from .calculadora import sumar, restar, multiplicar, dividir

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    """
    Maneja la ruta principal de la aplicación.

    - Si el método es GET: muestra el formulario de la calculadora.
    - Si el método es POST: procesa los datos enviados, realiza la operación
      seleccionada (sumar, restar, multiplicar o dividir)
      y devuelve el resultado.

    Returns:
        str: El HTML renderizado de la página con el resultado.
    """
    resultado = None
    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            operacion = request.form["operacion"]

            if operacion == "sumar":
                resultado = sumar(num1, num2)
            elif operacion == "restar":
                resultado = restar(num1, num2)
            elif operacion == "multiplicar":
                resultado = multiplicar(num1, num2)
            elif operacion == "dividir":
                resultado = dividir(num1, num2)
            else:
                resultado = "Operación no válida"
        except ValueError:
            resultado = "Error: Introduce números válidos"
        except ZeroDivisionError:
            resultado = "Error: No se puede dividir por cero"

    return render_template("index.html", resultado=resultado)


if __name__ == "__main__":  # pragma: no cover
    app.run(port=5000, host="0.0.0.0")
