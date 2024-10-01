        
# Components of another_year add up to exactly 365 days
# from datetime import timedelta
# year = timedelta(days=365)
# another_year = timedelta(weeks=40, days=84, hours=23, minutes=50, seconds=600)
# resultado = year.total_seconds() == another_year.total_seconds()
# resultado2 = year == another_year

# print(resultado,"---",resultado2)  

show = """
    1 - Cadastra
    2 - lista
    0 - Sair
"""
# Variável Global
carro = []

class Carro:
    def __init__(self,dono,cor,placa) -> None:
        self.dono = dono
        self.cor = cor
        self.placa = placa
        
    def __str__(self):
        return f"{self.__class__.__name__} : {','.join( [f" {i}: {r}" for i , r  in self.__dict__.items()] )}"
    
    
    
while True:
    print(show)
    op = input('Opção: ')
   
    if op == '1':
        dono =  input('Dono: ')
        cor =  input('Cor: ')
        placa =  input('Placa: ')

        car = Carro(dono, cor, placa)
        carro.append(car)
        
    elif op == '2':    
        print('######### LIsta De Carros ##########')
        for i in carro:
            print(f'Dono: {i.dono} Cor: {i.cor}')
        
    elif op == '0':
        break
    
    

    