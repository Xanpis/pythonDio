
class User:
    def __init__(self,name,placa) -> None:
        self.name = name
        self.placa = placa
        
    def __str__(self) -> str:
        return f"{__class__.__name__} {"  ".join([f"{chave}:{valor}" for chave,valor in self.__dict__.items()])}"
    
    
carro1 = User('joaninha', 121)
print(carro1)