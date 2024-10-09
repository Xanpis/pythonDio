

# Dados relacionados com o usuário e o carro 
class User: 
    def __init__(self,name,idade) -> None:
        self.name = name
        self.idade = idade

    def __str__(self) -> str:
        return f"Dono do carro = {" | ".join([f"{chave}: {valor}" for chave,valor in self.__dict__.items()]).title()}"
    
    
    
# Métodos para manipulação da classe User        
class Carro: 

    def __init__(self,user:User, cor , placa) -> None:
        self.user = user
        self.cor = cor
        self._placa = placa 
         
    def __str__(self) -> str:
            return f"{self.user} | Cor: {self.cor} | Placa: {self._placa}"
        
        
    # encapsulamento
    @property
    def placa(self):
        return self._placa or 0
    
    @placa.setter
    def placa(self, placa:int):
        try:
            if placa == 1:
                self._placa   # olhar porque o exception não esta funcionando                      
        except Exception as e:
            print(f'@@@ placa erro {e} @@@ {self.name} ')   
            
            
            
# métodos de manipulação 
class Cadastrados:
    def __init__(self) -> None:
        self.cadastro = [] 
        self.user =[]
        
    def add_user(self,obj:User):
        self.user.append(obj)
        pass
            
    def add_carro(self,obj:Carro):
        self.cadastro.append(obj)
    
    def buscar_user_carro(self,placa:int):
        placaUser = "".join([f"{chave}" for chave in self.cadastro if chave.placa == placa])    
        return placaUser or False     
    
    
        
ca = Cadastrados()
user = User('maria',23)
ca.add_user(user)

carro = Carro(user,'verde',123)
ca.add(carro)


print(ca.buscarUser(345))
print(100 * '-')
print(carro.user.idade)



