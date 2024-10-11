car,user = [],[]


# Classe para usuário 
class User: 
    try:
        def __init__(self, name, idade) -> None:
            if not self.validar_nome(name):
                raise ValueError("Nome deve ser uma string e ser maior que 3 caracteres.")
            if not self.validar_idade(idade):
                raise ValueError("Idade deve ser um número inteiro positivo. E mair que 18")
            
            self.name = name
            self.idade = idade
    except:
        print('Nome ou idade incorreto')
        
    def __str__(self) -> str:
        return f"Dono do carro = {' | '.join([f'{chave}: {valor}' for chave, valor in self.__dict__.items()]).title()}"

    @staticmethod
    def validar_nome(nome):
        return isinstance(nome, str) and len(nome) >= 3

    @staticmethod
    def validar_idade(idade):
        return isinstance(idade, int) and idade >= 18
            
# Classe para cadastra o carro recebendo um objeto do tipo Usuário  
class Car: 

    def __init__(self,user:User, cor , placa) -> None:
        
        if not self.validar_placa(placa):
            raise ValueError("A placa dever ter exatamente 5 números positivos")
        
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
        return isinstance(placa, str) and len(placa) == 4
    
    
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
        

try:
    user = User('mu',23)
    print(user)
except ValueError as e :
    print(e)
    



