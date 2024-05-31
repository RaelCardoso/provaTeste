import pytest
from app.verifica_triangulo import verifica_triangulo


def test_nao_e_triangulo():
    assert verifica_triangulo(1, 1, 3) == 'Nao e um triangulo'
    assert verifica_triangulo(1, 2, 8) == 'Nao e um triangulo'
    assert verifica_triangulo(5, 1, 1) == 'Nao e um triangulo'


def test_triangulo_equilatero():
    assert verifica_triangulo(5, 5, 5) == 'Equilatero'


def test_triangulo_isosceles():
    assert verifica_triangulo(2, 2, 3) == 'Isosceles'
    assert verifica_triangulo(4, 4, 2) == 'Isosceles'
    assert verifica_triangulo(2, 3, 2) == 'Isosceles'


def test_triangulo_escaleno():
    assert verifica_triangulo(2, 3, 4) == 'Escaleno'
    assert verifica_triangulo(5, 6, 7) == 'Escaleno'
    assert verifica_triangulo(7, 10, 5) == 'Escaleno'
