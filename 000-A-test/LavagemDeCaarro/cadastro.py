

car,user = [],[]

# Classe para usuário 
class User: 
    try:
        def __init__(self, name, idade) -> None:
            if not self.validar_nome(name):
                raise ValueError("Nome deve ser uma string e ser maior que 3 caracteres.")
            if not self.validar_idade(idade):
                raise ValueError("Idade deve ser um número inteiro positivo. Mair que (18) e Menor que (70) ")
            
            self.name = name
            self.idade = idade
    except:
        print('Nome ou idade incorreto')
        
    def __str__(self) -> str:
        return f"Dono = {' | '.join([f'{chave}: {valor}' for chave, valor in self.__dict__.items()])}"

    @staticmethod
    def validar_nome(nome):
        return isinstance(nome, str) and len(nome) >= 3

    @staticmethod
    def validar_idade(idade):
        return isinstance(idade, int) and idade >= 18 and idade <= 70
    
    def buscando_user(self,nome:str):
        if not user:
            return '@@@ Erro Lista de Usuário vazia @@@'
        else:  
            for i in user:
                if i.name == nome:
                    return ValueError(i) 
                else:
                    raise ValueError("@@@ Erro nome não localizado @@@")  
                      

            
# Classe para cadastra o carro recebendo um objeto do tipo Usuário  
class Car: 

    def __init__(self,user:User, cor , placa) -> None:
        
        if not self.validar_placa(placa):
            raise ValueError("A placa dever ter exatamente 4 números positivos")
        
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
        # colocando str pora poder saber o tamanho por que com int não funciona
        return isinstance(placa, str) and len(placa) == 4
    
    
    def buscar_id_placa(self,placa:int):
        placaUser = "".join([f"{chave}" for chave in car if chave.placa == placa])    
        return placaUser or False  
              
      
class Trunk(Car):
    def __init__(self, user, cor, placa):
        super().__init__(user, cor, placa)


            
# métodos de manipulação 
class Lavar_cadastrados:
    def __init__(self, placa, tempo) -> None:
        
        if not self.validar_placa(placa):
            raise ValueError("A placa dever ter exatamente 4 números positivos")
        
        self.placa = placa
        self.tempo = self.validar_tempo(tempo)
        
    @staticmethod
    def validar_placa(placa: int) -> bool:
        return isinstance(placa, int) and len(placa) == 4
    
    # Tempo para os carros ficarem prontos
    @staticmethod
    def validar_tempo(tempo) -> bool:
        for i in car:
            if i.__class__.__name__== "Car":
                return  
    
try:
    use = User('porch',28)
    print(use)
    user.append(use)
except ValueError as e:
    print(e)

    
try:
    print(use.buscando_user("mu"))
except ValueError as e:
    print(e)


try:
    tru = Trunk(use,'verde','1234')
    print(tru)
except ValueError as e:
    print(e)
    

    


