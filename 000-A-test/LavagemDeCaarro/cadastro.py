car,user = [],[]


# Classe para usuário 
class User: 
    def __init__(self,name,idade) -> None:
        self.name = name
        self.idade = idade

    def __str__(self) -> str:
        return f"Dono do carro = {" | ".join([f"{chave}: {valor}" for chave,valor in self.__dict__.items()]).title()}"

    @staticmethod
    def validar_nome(nome):
        return isinstance(nome,int) and len(nome) == 5
            
# Classe para cadastra o carro recebendo um objeto do tipo Usuário  
class Car: 

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
            if isinstance(placa,int()):
                self._placa   # olhar porque o exception não esta funcionando                      
        except Exception as e:
            print(f'@@@ placa erro {e} @@@ {self.name} ')   
            
    # Método para validar classe sem precisar instanciar a classe                    
    @staticmethod
    def validar_placa(placa: str) -> bool:
        return isinstance(placa, str) and len(placa) == 7
    
    def buscar_id_placa(self,placa:int):
        placaUser = "".join([f"{chave}" for chave in car if chave.placa == placa])    
        return placaUser or False  
     
       
            
    
      
class Trunk(Car):
    pass


            
# métodos de manipulação 
class Lavagem_cadastrados:
    def __init__(self) -> None:
        pass
    
    def add_user(self,obj:User):
        self.user.append(obj)

            
    def add_carro(self,obj:Car):
        self.cadastro.append(obj)
    
    def buscar_user_carro(self,placa:int):
        placaUser = "".join([f"{chave}" for chave in car if chave.placa == placa])    
        return placaUser or False     
    
    def show_all(self):
        for i in self.cadastro:
            print(100 * '-')
            print(i)
        
    
        
ca = Cadastrados()
user = User('maria',23)
ca.add_user(user)

# carro = Car(user,'verde',123)
# ca.add_carro(carro)

# user = User('Tues',26)
# ca.add_user(user)

# carro = Car(user,'verde',124)
# ca.add_carro(carro)




# print(ca.buscar_user_carro(123))
# print(100 * '-')
print(user)



