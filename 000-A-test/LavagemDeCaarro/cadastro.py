from datetime import  date, datetime, timedelta
carro_tempo = 1800
truck_tempo = 60
hora_data = datetime.now()

data_estimada = hora_data + timedelta(0,0,0,0,truck_tempo,)

print(data_estimada)

choses = f"""
[1] Cadastra Usuário
[2] Lista Usuário
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
        self.vei = []
    
    
    def __str__(self) -> str:
        if not self.vei:
            return f"User = Nome: {self.name} | idade: { self.idade}"
        else:
            # return f"User = Nome: {self.name} | idade: { self.idade} | {' '.join([f'Veiculo: {i.__class__.__name__} | Cor: {i.cor} | Placa: {i._placa}' for i in self.vei])}"
            return f"User = Nome: {self.name} | idade: { self.idade} | Veículos: {[f'Veiculo: {i.__class__.__name__}  Placa: {i.placa }  Cor: {i.cor} ' for i in self.vei]}"
                
    @staticmethod
    def validar_nome(nome):
        return isinstance(nome, str) and len(nome) >= 3

    @staticmethod
    def validar_idade(idade):
        return isinstance(idade, int) and idade >= 18 and idade <= 70
    
    def buscar_id_placa(self,placa:str):
        car = [i for i in self.vei if i.placa == placa]
        return car[0] if car else False

    def adicionar_carro(self,obj):
        self.vei.append(obj)    
    
                      
            
# Classe para cadastra o carro recebendo um objeto do tipo Usuário  
class Carro(): 
    def __init__(self, cor, placa):
        
        if not self.validar_placa(placa):
            raise ValueError("A placa dever ter exatamente 4 números positivos")
        
        self.cor = cor
        self._placa = placa 
         
    def __str__(self) -> str:
            return f" Veiculo: {self.__class__.__name__} | Cor: {self.cor} | Placa: {self._placa}"
                  
    # Método para validar classe sem precisar instanciar a classe                    
    @staticmethod
    def validar_placa(placa: str) -> bool:
        # colocando str para poder saber o tamanho por que com int não funciona
        return isinstance(placa, str) and len(placa) == 4
    
    @property
    def placa(self):
        return self._placa 
    
              
# Class caminhão      
class Trunk(Carro):
    def __init__(self, cor, placa):
        super().__init__(cor, placa)

           
# métodos de manipulação 
class Lavar_cadastrados:
    def __init__(self, array):
        self.array = array
        
    def add_lavagem(self,placa):
        for i in self.array:
                for j in i.vei:
                    if j.placa == placa:
                        car.append(f"Dono: {i.name} | {j}")
                    else:
                        raise ValueError("@@ Veiculo Não Encontrado @@")
            
       
    
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

#     if op == '3':
#         break
    
    
#     if op == '0':
        # break

# us = User('guio',34)
# yu = User("maria", 23)
# # print(us)
# t = Carro('verde', '1345')
# us.adicionar_carro(t)

# t = Carro('preto', '2345')
# us.adicionar_carro(t)

# user.append(us)


# try:
#     lava = Lavar_cadastrados(user)
#     lava.add_lavagem('145')
#     print(car)
# except ValueError as e:
#     print(e)


    
# try:
#     print(use.buscando_user("mu"))
# except ValueError as e:
#     print(e)


# try:
#     tru = Trunk(use,'verde','1234')
#     print(tru)
# except ValueError as e:
#     print(e)