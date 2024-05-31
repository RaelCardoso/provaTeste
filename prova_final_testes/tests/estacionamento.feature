Feature: Controle de Estacionamento

  Scenario: emitir um ticket para entrada de veiculo
    given um veiculo entra no estacionamento
    when o frentista emite um ticket para o veiculo
    then o ticket contem informacoes corretas sobre a entrada do veiculo

  Scenario: calcular o valor devido para a saida de veiculo
    given um veiculo esta estacionado ha 2 horas
    when o cliente apresenta o ticket de entrada para a saida
    then o frentista calcula o valor devido corretamente
