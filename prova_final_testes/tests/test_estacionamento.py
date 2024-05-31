"""Controle de Estacionamento"""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)
from datetime import datetime, timedelta
import pytest
from app.estacionamento import Estacionamento
from app.ticket import Ticket


@pytest.fixture
def estacionamento():
    return Estacionamento()


@scenario('estacionamento.feature', 'emitir um ticket para entrada de veiculo')
def test_emitir_um_ticket_para_entrada_de_veiculo():
    """emitir um ticket para entrada de veiculo."""


@given('um veiculo entra no estacionamento')
def veiculo_entra():
    """um veiculo entra no estacionamento."""
    return Ticket(placa="ABC-1234", modelo="Carro Teste")


@when('o frentista emite um ticket para o veiculo')
def emite_ticket(veiculo_entra, estacionamento):
    """o frentista emite um ticket para o veiculo."""
    estacionamento.emitir_tickets(veiculo_entra)


@then('o ticket contem informacoes corretas sobre a entrada do veiculo')
def verifica_ticket(veiculo_entra):
    """o ticket contem informacoes corretas sobre a entrada do veiculo."""
    assert veiculo_entra.placa == "ABC-1234"
    assert veiculo_entra.modelo == "Carro Teste"
    assert veiculo_entra.entrada is not None


@scenario('estacionamento.feature', 'calcular o valor devido para a saida de veiculo')
def test_calcular_o_valor_devido_para_a_saida_de_veiculo():
    """calcular o valor devido para a saida de veiculo."""


@given('um veiculo esta estacionado ha 2 horas')
def veiculo_estacionado():
    """um veiculo esta estacionado ha 2 horas."""
    entrada = datetime.now() - timedelta(hours=2)
    return Ticket(placa="XYZ-9876", modelo="Carro Teste", entrada=entrada)


@when('o cliente apresenta o ticket de entrada para a saida')
def apresenta_ticket(veiculo_estacionado, estacionamento):
    """o cliente apresenta o ticket de entrada para a saida."""
    estacionamento.registrar_saida(veiculo_estacionado)


@then('o frentista calcula o valor devido corretamente')
def calcula_valor(estacionamento, veiculo_estacionado):
    """o frentista calcula o valor devido corretamente."""
    valor = estacionamento.calcular_valor_devido(veiculo_estacionado)
    assert valor == 20  # 15 + 5 (para as horas adicionais)
