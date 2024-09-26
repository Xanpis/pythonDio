from class_carro import Carro

# Variável Global
carro = {}

# Adicionar um novo usuário
def add():
    dono =  input('\nDono: ')
    cor =  input('Cor: ')
    placa =  input('Placa: ')

    car = Carro(dono, cor, placa)
    carro[car.dono] = {'cor':car.cor , 'placa': car.placa}    
    

# Lista usuários
def lista():
    print('\n==================== LIsta De Carros ====================\n')
    for a,b in carro.items():
        print(f"Dono: {a} | Cor: {b['cor']} | Placa: {b['placa']}")
        print('--------------------------------------------------------')
    
# remover
def remover():
    lista()
    chave = input('\nDigite a placa: ')
    var = None
    # placa = ''
    
    for a,b  in carro.items():     
        if chave == b['placa']:
           var = a 
        #    placa = b['placa']
   
    if var is not None:
        del carro[var]
        print('\nRemovido!!')
    else:
        print("\nEro!! Placa não encontrada")
        
    
       
    
    
            