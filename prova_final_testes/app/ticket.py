from datetime import datetime


class Ticket:
    def __init__(self, placa, modelo, entrada=None, saida=None):
        self.placa = placa
        self.modelo = modelo
        self.entrada = entrada or datetime.now()
        self.saida = saida
