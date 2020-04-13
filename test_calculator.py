"""
Unit tests for the calculator library
"""

from calculadora import *


class TestCalculadora:
    def __init__(self):
        this.calculadora = Calculadora()

    def test_suma(self):
        assert 4 == this.calculadora.sumar(2, 2)

    def test_resta(self):
        assert 2 == this.calculadora.restar(4, 2)
