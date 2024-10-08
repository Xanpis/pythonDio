

# Dados relacionados com o usuário e o carro 
class User: 
    def __init__(self,name,placa) -> None:
        self.name = name
        self._placa = placa
        
    def __str__(self) -> str:
        return f"Dono do carro = {" | ".join([f"{chave}: {valor}" for chave,valor in self.__dict__.items()]).title()}"
    
    @property
    def placa(self):
        return self._placa or 0
    
    @placa.setter
    def placa(self,placa):
        try:
            if placa == 1:
                self._placa                          
        except Exception as e:
            print(f'@@@ placa erro {e} @@@ {self.name} ')   
            

    
# funções para manipulação da classe User   
class Cadastros(): 
    def __init__(self) -> None:
        self._cadastrados = []   
    
    def add(self,obj):
        self._cadastrados.append(obj)
    
    def buscarUser(self,placa):
        placaUser = "".join([f"{chave}" for chave in self._cadastrados if chave._placa == placa])    
        return placaUser or False
  
    
ca = Cadastros()

carro = User('joaninha', 123)
ca.add(carro)

carro = User('joão', 125)
ca.add(carro)
carro.placa = 2

print(carro)

