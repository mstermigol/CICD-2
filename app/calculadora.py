"""
Módulo de operaciones aritméticas básicas.

Contiene funciones para sumar, restar, multiplicar y dividir dos números.
Incluye manejo de errores para la división entre cero.
"""


def sumar(a, b):
    """Devuelve la suma de a y b."""
    return a + b


def restar(a, b):
    """Devuelve la resta de a menos b."""
    return a - b


def multiplicar(a, b):
    """Devuelve el producto de a y b."""
    return a * b


def dividir(a, b):
    """Devuelve la división de a entre b.

    Lanza:
        ZeroDivisionError: Si b es 0.
    """
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a / b


def potencia(a, b):
    """Devuelve a elevado a la potencia de b."""
    return a**b


def raiz_cuadrada(a):
    """Devuelve la raíz cuadrada de a.

    Lanza:
        ValueError: Si a es negativo.
    """
    if a < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")
    return a**0.5
