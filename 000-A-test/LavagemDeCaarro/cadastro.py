

# pegando os dados dos usuários e seu carro 
class User: 
    def __init__(self,name,placa) -> None:
        self.name = name
        self._placa = placa
        
    @property
    def placa(self):
        return self._placa
    
    @placa.setter
    def placa(self,placa):
        try:
            if placa == 1:
                self._placa 
                    
        except:
            print(f'@@@ placa erro @@@ {self.name}')   
            
    def __str__(self) -> str:
        return f"Dono do carro = {" | ".join([f"{chave}: {valor}" for chave,valor in self.__dict__.items()]).title()}"

    
# Manipulando os dados   
class Cadastros(): 
    def __init__(self) -> None:
        self._cadastrados = [] 
        
    
    def add(self,obj):
        self._cadastrados.append(obj)
    
    def buscarUser(self,placa):
        placaUser = "".join([f"{chave}" for chave in self._cadastrados if chave._placa == placa])   
           
        return placaUser or False
  
    
ca = Cadastros()
carro1 = User('joaninha', 123)
ca.add(carro1)

carro1 = User('joão', 125)
ca.add(carro1)
carro1.placa = 2

print(carro1)

