from class_carro import Carro

# Variável Global
carro = {}

# Adicionar um novo usuário
def add():
    dono =  input('Dono: ')
    cor =  input('Cor: ')
    placa =  input('Placa: ')

    car = Carro(dono, cor, placa)
    carro[car.dono] = {'cor':car.cor , 'placa': car.placa}    
    

# Lista usuários
def lista():
    print('######### LIsta De Carros ##########\n')
    for a,b in carro.items():
        print(f"Dono: {a} | Cor: {b['cor']} | Placa: {b['placa']}")
        print('--------------------------------------------------------')
    
# remover
def remover():
    chave = input('Digite a placa: ')
    for a,b  in carro.values()
        if chave in b['placa']:
            carro[a]
        