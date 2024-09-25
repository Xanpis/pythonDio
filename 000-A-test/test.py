        
# Components of another_year add up to exactly 365 days
# from datetime import timedelta
# year = timedelta(days=365)
# another_year = timedelta(weeks=40, days=84, hours=23, minutes=50, seconds=600)
# resultado = year.total_seconds() == another_year.total_seconds()
# resultado2 = year == another_year

# print(resultado,"---",resultado2)  

class Carro:
    def __init__(self,dono,cor,placa) -> None:
        self.dono = dono
        self.cor = cor
        self.placa = placa
        
    def __str__(self):
        return self.__class__.__name__
    
    
carro = Carro('guio','verde',23) 
print(carro)