# keyword arguments - keyword-only: o que vem Depois do (*) é obrigatorio ser nomeado,
# O que vem ANTES da (/) é obrigatorio ser por posicao


def criar_carro(modelo, ano, placa, /, *, marca, motor, combustivel, ):
    print(modelo, ano, placa, marca, motor, combustivel)
    
    
# invalido
# criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
# valido
criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") 
# Invalido
# criar_carro("Palio", 1999, "ABC-1234", "Fiat", "1.0", "Gasolina") 