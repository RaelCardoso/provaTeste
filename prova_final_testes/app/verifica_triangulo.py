def verifica_triangulo(a, b, c):
    # testando se é triangulo
    if (a + b < c) or (a + c < b) or (b + c < a):
        return 'Nao e um triangulo'
    elif (a == b) and (a == c):
        return 'Equilatero'
    elif (a == b) or (a == c) or (b == c):
        return 'Isosceles'
    else:
        return 'Escaleno'
