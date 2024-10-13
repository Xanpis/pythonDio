choses = f"""
[1] Cadastra Usuário
[2] Lista Usuário
[] Trocar O Nome Do Usuário
[] Deletar Usuário
[] Cadastra Carro
[] Cadastra Caminhão
[] Buscar Veiculo
[] Deletar veiculo
[] Lavar Veiculo
[] Retira Veiculo da Lavagem
[0] Sair
"""

# Classe para usuário 
class User: 
    def __init__(self, name, idade) -> None:
        if not self.validar_nome(name):
            raise ValueError("@@ Nome deve ser uma string e ser maior que 3 caracteres.@@")
        if not self.validar_idade(idade):
            raise ValueError("@@ Idade deve ser um número inteiro positivo. Mair que (18) e Menor que (70) @@")
        
        self.name = name
        self.idade = idade
  
        
    def __str__(self) -> str:
        return f"User = {' | '.join([f'{chave}: {valor}' for chave, valor in self.__dict__.items()])}"

    @staticmethod
    def validar_nome(nome):
        return isinstance(nome, str) and len(nome) >= 3

    @staticmethod
    def validar_idade(idade):
        return isinstance(idade, int) and idade >= 18 and idade <= 70
    
                      
            
# Classe para cadastra o carro recebendo um objeto do tipo Usuário  
class Car(): 
    def __init__(self, cor, placa):
        
        if not self.validar_placa(placa):
            raise ValueError("A placa dever ter exatamente 4 números positivos")
        
        self.cor = cor
        self._placa = placa 
         
    def __str__(self) -> str:
            return f"| Veiculo: {self.__class__.__name__} | Cor: {self.cor} | Placa: {self._placa}"
         
            
    # Método para validar classe sem precisar instanciar a classe                    
    @staticmethod
    def validar_placa(placa: str) -> bool:
        # colocando str para poder saber o tamanho por que com int não funciona
        return isinstance(placa, str) and len(placa) == 4
    
    
    def buscar_id_placa(self,placa:int):
        placaUser = "".join([f"{chave}" for chave in car if chave.placa == placa])    
        return placaUser or False  

              
# Class caminhão      
class Trunk(Car):
    def __init__(self, cor, placa):
        super().__init__(cor, placa)

           
# métodos de manipulação 
class Lavar_cadastrados:
    def __init__(self, user, placa, tempo) -> None:
        
        # if not self.validar_placa(placa):
        #     raise ValueError("A placa dever ter exatamente 4 números positivos")
        self.user = user
        self.placa = placa
        self.tempo = self.validar_tempo(tempo)
        
    def __str__(self) -> str:
        return f"{self.user} | Tempo:{self.placa}"
        
    # @staticmethod
    # def validar_placa(placa: str) -> bool:
    #     return isinstance(placa, str) and len(placa) == 4
    
    # Tempo para os carros ficarem prontos
    @staticmethod
    def validar_tempo(tempo) -> bool:
        for i in car:
            if i.__class__.__name__== "Car":
                return  
    
    
car,user = [],[]
# while True:
#     op = input(f"{choses}> " )

#     if op == '1':
#         nome = input("Nome: ")
#         idade =int(input("Idade: "))
#         try:
#             use = User(nome,idade)
#             user.append(use)
#             print("## Usuário Cadastrado ##")
#         except ValueError as e:
#             print(e)

#     if op == '2':
#         if not user:
#             print("@@@ Não tem Usuário cadastrado @@@")
#         else:
#             for i in user:
#                 print(50* "-")
#                 print(i)

#     if op == '0':
#         break

us = User('guio',34)
t = Car('verde', '1345')
print(us)




    





    
# try:
#     print(use.buscando_user("mu"))
# except ValueError as e:
#     print(e)


# try:
#     tru = Trunk(use,'verde','1234')
#     print(tru)
# except ValueError as e:
#     print(e)