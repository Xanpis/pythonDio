
class Carro:
    def __init__(self,dono,cor,placa) -> None:
        self.dono = dono
        self.cor = cor
        self.placa = placa
        
    def __str__(self):
        return f"{self.__class__.__name__} : {','.join( [f" {i}: {r}" for i , r  in self.__dict__.items()] )}"
    
    

    
