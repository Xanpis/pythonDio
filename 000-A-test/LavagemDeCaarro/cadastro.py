from datetime import  date, datetime, timedelta
carro_tempo = 30
truck_tempo = 60
hora_data = datetime.now()


choses = f"""
[1] Cadastra Usuário
[2] Lista Usuário
[3] Deletar Usuário
[4] Cadastra Carro
[5] Cadastra Caminhão
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
            raise ValueError("A placa dever ter maior ou igual 4 Carácter números e letra")
        
        self.cor = cor
        self._placa = placa 
         
    def __str__(self) -> str:
            return f" Veiculo: {self.__class__.__name__} | Cor: {self.cor} | Placa: {self._placa}"
                  
    # Método para validar classe sem precisar instanciar a classe                    
    @staticmethod
    def validar_placa(placa: str) -> bool:
        # colocando str para poder saber o tamanho por que com int não funciona
        return isinstance(placa, str) and len(placa) >= 4
    
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
                if placa == j.placa:
                    if j.__class__.__name__ == 'Carro':
                        car.append(f"Dono: {i.name} | {j} Chegada: {hora_data}  Saida: {hora_data +timedelta(0,0,0,0,carro_tempo)}")
                    if j.__class__.__name__ == 'Trunk':
                        car.append(f"Dono: {i.name} | {j} Chegada: {hora_data}  Saida: {hora_data +timedelta(0,0,0,0,truck_tempo)}")
                
                        
                              
    
array_car,array_user = [],[]

def mostra_user():
    if not array_user:
        print("@@@ Não tem Usuário cadastrado @@@")
        return False
    else:
        for i in array_user:
            print(50* "-")
            print(i)
    return True        
def buscar_user(nome):
    for i in array_user:
        if i.name == nome:
            print(i)
            return i 

def deletar_user(nome):
    j = 0
    for i in array_user:
        j+=1
        if i.name == nome:
            array_user.pop(j-1)
            print("Removido")

    
while True:
    op = input(f"{choses}> " )

    if op == '1':
        nome = input("Nome: ")
        try:
            idade =int(input("Idade: "))
            user = User(nome,idade)
            array_user.append(user)
            print("## Usuário Cadastrado ##")
        except ValueError as e:
            print(e)

    if op == '2':
        mostra_user()

    if op == '3':
        try:
          nome = input("Informe o Nome do Usuário para ser Removido: ")
          deletar_user(nome)
        except:
            pass

    
    if op == '4':
            
        try:
            e = mostra_user()
            if not e :
                pass
            else:   
                print() 
                nome = input("Informe o Nome do Usuário para Adicionar o carro: ")
                i = buscar_user(nome)
                if not i :
                    print("@@ Usuário não encontrado") 
                else:
                    cor = input("Informe a Cor do Carro: ")
                    placa = input("Informe a Placa Com 4 Numero ou Letra: ")
                    carro = Carro(cor,placa)
                    i.adicionar_carro(carro)
                    print("## Carro cadastrado ##")
        except ValueError as e:
            print(e)

    
    if op == '5':
            
        try:
            e = mostra_user()
            if not e :
                pass
            else:   
                print() 
                nome = input("Informe o Nome do Usuário para Adicionar o Caminhão: ")
                i = buscar_user(nome)
                if not i :
                    print("@@ Usuário não encontrado") 
                else:
                    cor = input("Informe a Cor do Caminhão: ")
                    placa = input("Informe a Placa Com 4 Numero e Letra: ")
                    trunk = Trunk()(cor,placa)
                    i.adicionar_carro(trunk)
                    print("## Caminhão cadastrado ##")
        except ValueError as e:
            print(e)
        
        
        break
    
    
    if op == '0':
        break

# us = User('guio',34)
# yu = User("maria", 23)
# # print(us)
# t = Carro('verde', '1345')
# us.adicionar_carro(t)

# t = Carro('preto', '2345')
# us.adicionar_carro(t)

# user.append(us)

# print(user[0])

# try:
#     lava = Lavar_cadastrados(user)
#     lava.add_lavagem('1345')
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