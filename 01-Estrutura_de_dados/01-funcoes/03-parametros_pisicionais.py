
# keyword arguments: o que vem ANTES da (/) é obrigatorio ser por posicao, o que vem depois é opcional 
def criar_carro(ano, modelo, placa, / , marca, motor, combustivel, ):
    print(modelo, ano, placa, marca, motor, combustivel)
    
criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # valido
criar_carro("Palio", 1999, "ABC-1234", "Fiat", "1.0", "Gasolina") # valido
criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # inválido