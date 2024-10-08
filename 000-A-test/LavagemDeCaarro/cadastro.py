
class User: 
    def __init__(self,name,placa) -> None:
        self.name = name
        self.placa = placa
        
    def __str__(self) -> str:
        return f"{"  ".join([f"{chave}:{valor}" for chave,valor in self.__dict__.items()])}"
    
    

    
class Cadastros(): 
    def __init__(self) -> None:
        self.cadastrados = [] 
    
    def add(self,obj):
        self.cadastrados.append(obj)
    
    def buscarUser(self,placa):
        placaUser = "".join([f"{chave}" for chave in self.cadastrados if chave.placa == placa])   
           
        return placaUser or False
  
    
ca = Cadastros()
carro1 = User('joaninha', 123)
ca.add(carro1)

carro1 = User('joaninha', 125)
ca.add(carro1)

print(ca.buscarUser(123))