"""
Unit tests for the calculator library
"""

from calculadora import *


class TestCalculadora:

    def test_suma(self):
        this.calculadora = Calculadora()
        assert 4 == this.calculadora.sumar(2, 2)

    def test_resta(self):
        this.calculadora = Calculadora()
        assert 2 == this.calculadora.restar(4, 2)
